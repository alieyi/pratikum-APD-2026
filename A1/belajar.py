angka_benar = 7
while True:
    print("=====Game Tebak Angka=====")

    angka_input = int(input("Tebak angka antara 1 sampai 10: "))

    if angka_input == angka_benar:
        print("Selamat! Tebakanmu benar.")
        break
    else:
        print("Tebakanmu salah. Coba lagi!")