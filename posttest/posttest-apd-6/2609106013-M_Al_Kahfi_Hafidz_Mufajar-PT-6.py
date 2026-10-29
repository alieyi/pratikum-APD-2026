import os

users = {
    "admin": {"password": "admin17", "role": "admin"},
    "kasir": {"password": "kasir17", "role": "user"},
}

produk = {
    "P001": {"nama": "Indomie Goreng", "harga": 3500, "stok": 50},
    "P002": {"nama": "Aqua 600ml", "harga": 4000, "stok": 40},
    "P003": {"nama": "Roti Tawar", "harga": 15000, "stok": 10},
    "P004": {"nama": "Susu UHT 250ml", "harga": 6500, "stok": 25},
}


keranjang = {}

huruf = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
angka = set("0123456789")
huruf_angka = huruf | angka

user_aktif = ""
program_jalan = True

while program_jalan:
    os.system("cls" if os.name == "nt" else "clear")

    garis = "-" * 48
    tabel = []
    tabel.append("No " + "| " + "Kode  " + "| " + "Nama" + " " * 14 + "| " + "  Harga" + " | " + " Stok")
    tabel.append(garis)
    no = 1
    for kode in produk:
        n = str(no)
        nama = produk[kode]["nama"]
        harga = str(produk[kode]["harga"])
        stok = str(produk[kode]["stok"])
        baris = n + " " * (3 - len(n)) + "| "
        baris = baris + kode + " " * (6 - len(kode)) + "| "
        baris = baris + nama + " " * (18 - len(nama)) + "| "
        baris = baris + " " * (7 - len(harga)) + harga + " | "
        baris = baris + " " * (5 - len(stok)) + stok
        tabel.append(baris)
        no += 1
    tabel.append(garis)

    
    garis_k = "-" * 51
    tabel_k = []
    tabel_k.append("No " + "| " + "Nama" + " " * 14 + "| " + "  Harga" + " | " + " Qty" + " | " + " Subtotal")
    tabel_k.append(garis_k)
    total_k = 0
    no = 1
    for kode in keranjang:
        n = str(no)
        nama = produk[kode]["nama"]
        harga = str(produk[kode]["harga"])
        qty = str(keranjang[kode])
        subtotal = produk[kode]["harga"] * keranjang[kode]
        total_k += subtotal
        sub = str(subtotal)
        baris = n + " " * (3 - len(n)) + "| "
        baris = baris + nama + " " * (18 - len(nama)) + "| "
        baris = baris + " " * (7 - len(harga)) + harga + " | "
        baris = baris + " " * (4 - len(qty)) + qty + " | "
        baris = baris + " " * (9 - len(sub)) + sub
        tabel_k.append(baris)
        no += 1
    tabel_k.append(garis_k)
    tabel_k.append("TOTAL : Rp " + str(total_k))

    if user_aktif == "":
        print("=" * 40)
        print("   SISTEM KASIR MINIMARKET")
        print("=" * 40)
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print("\n--- LOGIN ---")
            print("(ketik 'exit' untuk kembali)")
            percobaan = 0
            batal = False
            while percobaan < 3 and user_aktif == "":
                username = input("Username : ")
                if username.lower() == "exit":
                    batal = True
                    break
                password = input("Password : ")
                if password.lower() == "exit":
                    batal = True
                    break

                if username in users and users[username]["password"] == password:
                    user_aktif = username
                    keranjang = {}
                else:
                    percobaan += 1
                    print("Username atau password salah! Sisa:", 3 - percobaan)

            if user_aktif != "":
                print("Login berhasil! Selamat datang,", user_aktif)
            elif batal:
                print("Login dibatalkan.")
            else:
                print("Login gagal 3x. Program ditutup.")
                program_jalan = False

        elif pilihan == "2":
            print("\n--- REGISTER ---")
            print("(ketik 'exit' untuk kembali)")
            batal = False

            while True:
                username = input("Username baru : ")
                if username.lower() == "exit":
                    batal = True
                    break
                if username == "":
                    print("Username tidak boleh kosong!")
                elif " " in username:
                    print("Username tidak boleh ada spasi!")
                elif username in users:
                    print("Username sudah dipakai!")
                else:
                    break

            if not batal:
                while True:
                    password = input("Password baru : ")
                    if password.lower() == "exit":
                        batal = True
                        break
                    if len(password) < 4:
                        print("Password minimal 4 karakter!")
                    else:
                        break

            if not batal:
                users[username] = {"password": password, "role": "user"}
                print("Register berhasil! Silakan login.")
            else:
                print("Register dibatalkan.")

        elif pilihan == "0":
            print("Terima kasih, program selesai.")
            program_jalan = False

        else:
            print("Pilihan tidak valid!")

    elif users[user_aktif]["role"] == "admin":
        print("=" * 40)
        print("   MENU ADMIN | Login:", user_aktif)
        print("=" * 40)
        print("1. Tambah Produk")
        print("2. Tampilkan Daftar Produk")
        print("3. Cek Stok Produk")
        print("4. Ubah Harga/Stok Produk")
        print("5. Hapus Produk")
        print("0. Logout")
        pilihan = input("Pilih menu: ")
        print()

        if pilihan == "1":
            print("--- TAMBAH PRODUK ---")
            for baris in tabel:
                print(baris)
            print("(ketik 'exit' untuk batal)")
            batal = False

            while True:
                kode = input("Kode produk : ").upper()
                if kode == "EXIT":
                    batal = True
                    break
                if kode == "":
                    print("Kode tidak boleh kosong!")
                elif not set(kode) <= huruf_angka:
                    print("Kode hanya boleh huruf dan angka, tanpa spasi/simbol!")
                elif len(set(kode) & huruf) == 0 or len(set(kode) & angka) == 0:
                    print("Kode harus gabungan huruf dan angka! Contoh: P005")
                elif len(kode) > 6:
                    print("Kode maksimal 6 karakter!")
                elif kode in produk:
                    print("Kode produk sudah ada!")
                else:
                    break

            if not batal:
                while True:
                    nama = input("Nama produk : ")
                    if nama.lower() == "exit":
                        batal = True
                        break
                    if nama == "":
                        print("Nama tidak boleh kosong!")
                    elif len(nama) > 18:
                        print("Nama maksimal 18 karakter!")
                    else:
                        break

            if not batal:
                while True:
                    harga = input("Harga       : ")
                    if harga.lower() == "exit":
                        batal = True
                        break
                    if not harga.isdigit():
                        print("Harga harus angka!")
                    elif int(harga) < 1000:
                        print("Harga minimal Rp1000!")
                    else:
                        break

            if not batal:
                while True:
                    stok = input("Stok        : ")
                    if stok.lower() == "exit":
                        batal = True
                        break
                    if not stok.isdigit():
                        print("Stok harus angka!")
                    else:
                        break

            if not batal:
                produk[kode] = {"nama": nama, "harga": int(harga), "stok": int(stok)}
                print("\nProduk berhasil ditambahkan!")
            else:
                print("\nTambah produk dibatalkan.")

        elif pilihan == "2":
            print("--- DAFTAR PRODUK ---")
            if len(produk) == 0:
                print("Belum ada produk.")
            else:
                for baris in tabel:
                    print(baris)

        elif pilihan == "3":
            print("--- CEK STOK ---")
            for baris in tabel:
                print(baris)
            print("(ketik 'exit' untuk batal)")
            while True:
                kode = input("Masukkan kode produk: ").upper()
                if kode == "EXIT":
                    print("Dibatalkan.")
                    break
                if kode not in produk:
                    print("Produk tidak ditemukan!")
                    continue
                print(produk[kode]["nama"], "-> stok tersisa:", produk[kode]["stok"])
                if produk[kode]["stok"] == 0:
                    print("(Stok HABIS)")
                elif produk[kode]["stok"] <= 5:
                    print("(Stok menipis!)")
                break

        elif pilihan == "4":
            print("--- UBAH HARGA / STOK ---")
            for baris in tabel:
                print(baris)
            print("(ketik 'exit' untuk batal)")
            batal = False

            while True:
                kode = input("Masukkan kode produk: ").upper()
                if kode == "EXIT":
                    batal = True
                    break
                if kode not in produk:
                    print("Produk tidak ditemukan!")
                else:
                    break

            if not batal:
                print("\nProduk :", produk[kode]["nama"])
                print("Harga  :", produk[kode]["harga"])
                print("Stok   :", produk[kode]["stok"])
                print("1. Ubah Harga")
                print("2. Ubah Stok")

                while True:
                    sub = input("Pilih (1/2): ")
                    if sub.lower() == "exit":
                        batal = True
                        break
                    if sub == "1" or sub == "2":
                        break
                    print("Pilihan tidak valid!")

            if not batal:
                if sub == "1":
                    while True:
                        baru = input("Harga baru: ")
                        if baru.lower() == "exit":
                            batal = True
                            break
                        if not baru.isdigit():
                            print("Harga harus angka!")
                        elif int(baru) < 1000:
                            print("Harga minimal Rp1000!")
                        else:
                            break
                    if not batal:
                        produk[kode]["harga"] = int(baru)
                        print("\nHarga berhasil diubah!")
                else:
                    while True:
                        baru = input("Stok baru: ")
                        if baru.lower() == "exit":
                            batal = True
                            break
                        if not baru.isdigit():
                            print("Stok harus angka!")
                        else:
                            break
                    if not batal:
                        produk[kode]["stok"] = int(baru)
                        print("\nStok berhasil diubah!")

            if batal:
                print("\nUbah produk dibatalkan.")

        elif pilihan == "5":
            print("--- HAPUS PRODUK ---")
            if len(produk) == 0:
                print("Belum ada produk.")
            else:
                for baris in tabel:
                    print(baris)
                print("(ketik 'exit' untuk batal)")
                batal = False
                while True:
                    kode = input("Masukkan kode produk yang dihapus: ").upper()
                    if kode == "EXIT":
                        batal = True
                        break
                    if kode not in produk:
                        print("Produk tidak ditemukan!")
                    else:
                        break

                if not batal:
                    yakin = input("Yakin hapus '" + produk[kode]["nama"] + "'? (y/n): ")
                    if yakin.lower() == "y":
                        produk.pop(kode)
                        print("\nProduk berhasil dihapus!")
                    else:
                        print("\nPenghapusan dibatalkan.")
                else:
                    print("\nPenghapusan dibatalkan.")

        elif pilihan == "0":
            user_aktif = ""
            print("Logout berhasil.")

        else:
            print("Pilihan tidak valid!")

    else:
        print("=" * 40)
        print("   MENU PENGGUNA | Login:", user_aktif)
        print("=" * 40)
        print("1. Tampilkan Daftar Produk")
        print("2. Cek Stok Produk")
        print("3. Tambah Barang ke Keranjang")
        print("4. Lihat Keranjang")
        print("5. Ubah Jumlah di Keranjang")
        print("6. Batalkan Item Keranjang")
        print("7. Bayar & Cetak Struk")
        print("0. Logout")
        pilihan = input("Pilih menu: ")
        print()

        if pilihan == "1":
            print("--- DAFTAR PRODUK ---")
            if len(produk) == 0:
                print("Belum ada produk.")
            else:
                for baris in tabel:
                    print(baris)

        elif pilihan == "2":
            print("--- CEK STOK ---")
            for baris in tabel:
                print(baris)
            print("(ketik 'exit' untuk batal)")
            while True:
                kode = input("Masukkan kode produk: ").upper()
                if kode == "EXIT":
                    print("Dibatalkan.")
                    break
                if kode not in produk:
                    print("Produk tidak ditemukan!")
                    continue
                print(produk[kode]["nama"], "-> stok tersisa:", produk[kode]["stok"])
                break

        elif pilihan == "3":
            print("--- TAMBAH KE KERANJANG ---")
            for baris in tabel:
                print(baris)
            print("(ketik 'exit' untuk batal)")
            batal = False

            while True:
                kode = input("Kode produk : ").upper()
                if kode == "EXIT":
                    batal = True
                    break
                if kode not in produk:
                    print("Produk tidak ditemukan!")
                elif produk[kode]["stok"] == 0:
                    print("Maaf, stok produk habis!")
                else:
                    break

            if not batal:
                print("Produk :", produk[kode]["nama"], "(stok tersedia:", produk[kode]["stok"], ")")
                sudah = 0
                if kode in keranjang:
                    sudah = keranjang[kode]
                    print("(Sudah ada", sudah, "di keranjang)")

                while True:
                    jumlah = input("Jumlah beli : ")
                    if jumlah.lower() == "exit":
                        batal = True
                        break
                    if not jumlah.isdigit() or int(jumlah) <= 0:
                        print("Jumlah harus angka lebih dari 0!")
                    elif int(jumlah) > produk[kode]["stok"]:
                        print("Jumlah melebihi stok yang tersedia!")
                    else:
                        break

                if batal:
                    print("\nDibatalkan.")
                else:
                    jml_beli = int(jumlah)
                    keranjang[kode] = sudah + jml_beli
                    produk[kode]["stok"] -= jml_beli
                    print("\nBarang berhasil masuk keranjang!")
            else:
                print("\nDibatalkan.")

        elif pilihan == "4":
            print("--- ISI KERANJANG ---")
            if len(keranjang) == 0:
                print("Keranjang kosong.")
            else:
                for baris in tabel_k:
                    print(baris)

        elif pilihan == "5":
            print("--- UBAH JUMLAH BARANG ---")
            if len(keranjang) == 0:
                print("Keranjang kosong.")
            else:
                for baris in tabel_k:
                    print(baris)
                daftar = list(keranjang.keys())
                print("(ketik 'exit' untuk batal)")

                batal = False
                while True:
                    nomor = input("Pilih nomor item: ")
                    if nomor.lower() == "exit":
                        batal = True
                        break
                    if not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(daftar):
                        print("Nomor item tidak valid!")
                    else:
                        break

                if not batal:
                    kode = daftar[int(nomor) - 1]
                    qty_lama = keranjang[kode]
                    stok_tersedia = produk[kode]["stok"]
                    maks_beli = qty_lama + stok_tersedia

                    while True:
                        baru = input("Jumlah baru (maks " + str(maks_beli) + "): ")
                        if baru.lower() == "exit":
                            batal = True
                            break
                        if not baru.isdigit() or int(baru) <= 0:
                            print("Jumlah harus angka lebih dari 0!")
                        elif int(baru) > maks_beli:
                            print("Jumlah melebihi stok!")
                        else:
                            break
                    if batal:
                        print("\nDibatalkan.")
                    else:
                        qty_baru = int(baru)
                        produk[kode]["stok"] += (qty_lama - qty_baru)
                        keranjang[kode] = qty_baru
                        print("\nJumlah berhasil diubah!")
                else:
                    print("\nDibatalkan.")

        elif pilihan == "6":
            print("--- BATALKAN ITEM KERANJANG ---")
            if len(keranjang) == 0:
                print("Keranjang kosong.")
            else:
                for baris in tabel_k:
                    print(baris)
                daftar = list(keranjang.keys())
                print("(ketik 'exit' untuk batal)")

                batal = False
                while True:
                    nomor = input("Pilih nomor item yang dibatalkan: ")
                    if nomor.lower() == "exit":
                        batal = True
                        break
                    if not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(daftar):
                        print("Nomor item tidak valid!")
                    else:
                        break

                if not batal:
                    kode = daftar[int(nomor) - 1]
                    produk[kode]["stok"] += keranjang[kode]
                    print("\n'" + produk[kode]["nama"] + "' dibatalkan dari keranjang.")
                    keranjang.pop(kode)
                else:
                    print("\nDibatalkan.")

        elif pilihan == "7":
            print("--- PEMBAYARAN ---")
            if len(keranjang) == 0:
                print("Keranjang kosong, tidak ada yang dibayar.")
            else:
                for baris in tabel_k:
                    print(baris)
                print("(ketik 'exit' untuk batalkan)")

                batal = False
                while True:
                    bayar = input("Uang bayar : Rp ")
                    if bayar.lower() == "exit":
                        batal = True
                        break
                    if not bayar.isdigit():
                        print("Uang bayar harus angka!")
                    elif int(bayar) < total_k:
                        print("Uang tidak cukup!")
                    else:
                        break

                if not batal:
                    bayar = int(bayar)
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=" * 40)
                    print("        STRUK PEMBELIAN")
                    print("        MINIMARKET")
                    print("=" * 40)
                    print("Kasir :", user_aktif)
                    print("-" * 40)
                    for kode in keranjang:
                        qty = keranjang[kode]
                        harga = produk[kode]["harga"]
                        print(produk[kode]["nama"])
                        print("  ", qty, "x", harga, "=", qty * harga)
                    print("-" * 40)
                    print("TOTAL   : Rp", total_k)
                    print("BAYAR   : Rp", bayar)
                    print("KEMBALI : Rp", bayar - total_k)
                    print("=" * 40)
                    print("   Terima kasih sudah berbelanja!")
                    keranjang = {}
                else:
                    print("\nPembayaran dibatalkan.")

        elif pilihan == "0":
            if len(keranjang) > 0:
                for kode in keranjang:
                    produk[kode]["stok"] += keranjang[kode]
                print("Keranjang yang belum dibayar akan dikosongkan.")
            user_aktif = ""
            keranjang = {}
            print("Logout berhasil.")

        else:
            print("Pilihan tidak valid!")

    if program_jalan:
        input("\nTekan Enter untuk lanjut...")

        