# auth.py
# Login, register, logout

from colorama import Fore
from data import users, produk, keranjang, sesi
from validasi import input_valid, cek_username_baru, cek_password_baru


def proses_login():
    print("--- LOGIN ---")
    print("(ketik 'exit' untuk kembali)")
    percobaan = 0
    while percobaan < 3:
        username = input("Username : ")
        if username.lower() == "exit":
            print("Login dibatalkan.")
            return
        password = input("Password : ")
        if password.lower() == "exit":
            print("Login dibatalkan.")
            return
        try:
            if users[username]["password"] != password:
                raise ValueError("Password salah")
        except (KeyError, ValueError):
            percobaan += 1
            print(Fore.RED + "Username atau password salah! Sisa: " + str(3 - percobaan))
        else:
            sesi["user_aktif"] = username
            keranjang.clear()
            print(Fore.GREEN + "Login berhasil! Selamat datang, " + sesi["user_aktif"])
            return
    print("Login gagal 3x. Program ditutup.")
    sesi["program_jalan"] = False


def proses_register():
    print("--- REGISTER ---")
    print("(ketik 'exit' untuk kembali)")
    username = input_valid("Username baru : ", cek_username_baru)
    if username is None:
        print("Register dibatalkan.")
        return
    password = input_valid("Password baru : ", cek_password_baru)
    if password is None:
        print("Register dibatalkan.")
        return
    users[username] = {"password": password, "role": "user"}
    print(Fore.GREEN + "Register berhasil! Silakan login.")


def logout_user():
    if len(keranjang) > 0:
        for kode in keranjang:
            produk[kode]["stok"] += keranjang[kode]
        print("Keranjang yang belum dibayar akan dikosongkan.")
    keranjang.clear()
    sesi["user_aktif"] = ""
    print("Logout berhasil.")


def logout_admin():
    sesi["user_aktif"] = ""
    print("Logout berhasil.")
