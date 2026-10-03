USERNAME = "Al Kahfi"
NIM_3_DIGIT = "013"

PASSWORD = NIM_3_DIGIT
PIN = NIM_3_DIGIT * 2
MIN_TRANSFER = 50000
MAX_TRANSFER = 1000000
MAX_ATTEMPT = 3

saldo = 5000000

login_ok = False
percobaan = 1

while percobaan <= MAX_ATTEMPT and not login_ok:
    print("\n=== LOGIN (percobaan", percobaan, "/", MAX_ATTEMPT, ") ===")
    user = input("Username: ")
    pw = input("Password: ")

    if user == USERNAME and pw == PASSWORD:
        print("Login berhasil!")
        login_ok = True
    elif user != USERNAME and pw != PASSWORD:
        print("Username dan Password anda salah")
    elif user != USERNAME:
        print("Username anda salah")
    else:
        print("Password anda salah")

    percobaan += 1

if not login_ok:
    print("\nAkun anda diblokir karena 3x gagal login.")
else:

    running = True
    while running:
        print("\n=== MENU UTAMA ===")
        print("1. Transfer Uang")
        print("2. Cek Saldo / Rekening")
        print("3. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            transfer_lagi = True
            while transfer_lagi:
                print("\n=== TRANSFER UANG ===")
                print("Saldo saat ini: Rp", saldo)

                if saldo < MIN_TRANSFER:
                    print("Saldo tidak cukup untuk melakukan transfer.")
                    break

                penerima = input("Username penerima: ")

                while True:
                    teks = input("Masukkan nominal transfer: Rp")
                    if not teks.isdigit():
                        print("Nominal harus berupa angka bulat. Coba lagi.")
                    else:
                        nominal = int(teks)
                        if nominal < MIN_TRANSFER:
                            print("Nominal minimal Rp", MIN_TRANSFER)
                        elif nominal > MAX_TRANSFER:
                            print("Nominal maksimal Rp", MAX_TRANSFER)
                        elif nominal > saldo:
                            print("Saldo anda tidak mencukupi.")
                        else:
                            break

                pin_ok = False
                for i in range(1, MAX_ATTEMPT + 1):
                    pin = input("Masukkan PIN untuk konfirmasi: ")
                    if pin == PIN:
                        pin_ok = True
                        break
                    print("PIN salah! (kesempatan", i, "/", MAX_ATTEMPT, ")")

                if not pin_ok:
                    print("\nPIN salah 3x. Akun anda diblokir.")
                    running = False
                    break

                saldo = saldo - nominal
                print("\n===== STRUK BUKTI TRANSFER =====")
                print("Pengirim   :", USERNAME)
                print("Penerima   :", penerima)
                print("Nominal    : Rp", nominal)
                print("Sisa saldo : Rp", saldo)
                print("================================")

                while True:
                    lagi = input("\nApakah ingin transfer lagi (y/n)? ").lower()
                    if lagi == "y" or lagi == "n":
                        break
                    print("Masukkan 'y' atau 'n'.")

                if lagi == "n":
                    transfer_lagi = False

        elif pilihan == "2":
            print("\n=== INFO REKENING ===")
            print("Pemilik rekening:", USERNAME)
            print("Saldo saat ini  : Rp", saldo)

        elif pilihan == "3":
            print("Anda telah logout. Terima kasih!")
            running = False

        else:
            print("Pilihan tidak valid!")