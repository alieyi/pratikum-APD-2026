from colorama import init
from data import users, sesi
from tampilan import bersihkan_layar
from validasi import input_menu
from auth import proses_login, proses_register
from admin import menu_admin
from kasir import menu_user


def menu_awal():
    print("=" * 40)
    print("   SISTEM KASIR MINIMARKET")
    print("=" * 40)
    print("1. Login")
    print("2. Register")
    print("0. Keluar")
    pilihan = input_menu()
    if pilihan == "1":
        proses_login()
    elif pilihan == "2":
        proses_register()
    elif pilihan == "0":
        print("Terima kasih, program selesai.")
        sesi["program_jalan"] = False
    else:
        print("Pilihan tidak valid!")


def main():
    while sesi["program_jalan"]:
        bersihkan_layar()
        try:
            if sesi["user_aktif"] == "":
                menu_awal()
            elif users[sesi["user_aktif"]]["role"] == "admin":
                menu_admin()
            else:
                menu_user()
            if sesi["program_jalan"]:
                input("\nTekan Enter untuk lanjut...")
        except (KeyboardInterrupt, EOFError):
            print("\nProgram dihentikan paksa.")
            sesi["program_jalan"] = False


if __name__ == "__main__":
    init(autoreset=True) 
    main()
