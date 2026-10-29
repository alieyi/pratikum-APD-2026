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
user_aktif = ""
program_jalan = True

HURUF = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ANGKA = set("0123456789")


def input_menu():
    """Mengambil pilihan menu dari user."""
    pilihan = input("Pilih menu: ").strip()
    print()
    return pilihan


def hitung_total_keranjang():
    """Total belanja; memakai fungsi rekursif di bawah."""
    daftar_kode = list(keranjang.keys())
    return hitung_total_rekursif(daftar_kode)


def hitung_subtotal(kode):
    harga = produk[kode]["harga"]
    qty = keranjang[kode]
    return harga * qty


def hitung_total_rekursif(daftar_kode):
    """FUNGSI REKURSIF: menjumlahkan subtotal tiap item keranjang."""
    if len(daftar_kode) == 0:  # basis
        return 0
    return hitung_subtotal(daftar_kode[0]) + hitung_total_rekursif(daftar_kode[1:])


def input_angka(pesan, minimal=0, maksimal=None):
    """
    FUNGSI REKURSIF + ERROR HANDLING.
    Mengembalikan int, atau None jika user mengetik 'exit'.
    Jika input salah, fungsi memanggil dirinya sendiri lagi.
    """
    teks = input(pesan).strip()
    if teks.lower() == "exit":
        return None
    try:
        nilai = int(teks)
        if nilai < minimal:
            raise ValueError(f"Nilai minimal {minimal}!")
        if maksimal is not None and nilai > maksimal:
            raise ValueError(f"Nilai maksimal {maksimal}!")
    except ValueError as e:
        pesan_error = str(e)
        if "invalid literal" in pesan_error:
            pesan_error = "Input harus berupa angka!"
        print("Error:", pesan_error)
        return input_angka(pesan, minimal, maksimal)
    else:
        return nilai


def input_valid(pesan, validator):
    """
    FUNGSI REKURSIF + ERROR HANDLING.
    validator adalah fungsi yang akan raise ValueError kalau input salah.
    Mengembalikan hasil validator, atau None jika user mengetik 'exit'.
    """
    teks = input(pesan).strip()
    if teks.lower() == "exit":
        return None
    try:
        hasil = validator(teks)
    except ValueError as e:
        print("Error:", e)
        return input_valid(pesan, validator)
    else:
        return hasil


def cek_kode_baru(kode):
    kode = kode.upper()
    if kode == "":
        raise ValueError("Kode tidak boleh kosong!")
    if not set(kode) <= (HURUF | ANGKA):
        raise ValueError("Kode hanya boleh huruf dan angka!")
    if len(set(kode) & HURUF) == 0 or len(set(kode) & ANGKA) == 0:
        raise ValueError("Kode harus gabungan huruf dan angka! Contoh: P005")
    if len(kode) > 6:
        raise ValueError("Kode maksimal 6 karakter!")
    if kode in produk:
        raise ValueError("Kode produk sudah ada!")
    return kode


def cek_kode_ada(kode):
    kode = kode.upper()
    try:
        produk[kode]
    except KeyError:
        raise ValueError("Produk tidak ditemukan!")
    return kode


def cek_kode_ada_stok(kode):
    kode = cek_kode_ada(kode)
    if produk[kode]["stok"] == 0:
        raise ValueError("Maaf, stok produk habis!")
    return kode


def cek_nama(nama):
    if nama == "":
        raise ValueError("Nama tidak boleh kosong!")
    if len(nama) > 18:
        raise ValueError("Nama maksimal 18 karakter!")
    return nama


def cek_pilihan_12(teks):
    if teks not in ("1", "2"):
        raise ValueError("Pilihan harus 1 atau 2!")
    return teks


def cek_username_baru(username):
    if username == "":
        raise ValueError("Username tidak boleh kosong!")
    if " " in username:
        raise ValueError("Username tidak boleh ada spasi!")
    if username in users:
        raise ValueError("Username sudah dipakai!")
    return username


def cek_password_baru(password):
    if len(password) < 4:
        raise ValueError("Password minimal 4 karakter!")
    return password


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_produk():
    if len(produk) == 0:
        print("Belum ada produk.")
        return
    garis = "-" * 48
    print("No | Kode  | Nama" + " " * 14 + "|   Harga |  Stok")
    print(garis)
    no = 1
    for kode in produk:
        n = str(no)
        nama = produk[kode]["nama"]
        harga = str(produk[kode]["harga"])
        stok = str(produk[kode]["stok"])
        baris = n + " " * (3 - len(n)) + "| "
        baris += kode + " " * (6 - len(kode)) + "| "
        baris += nama + " " * (18 - len(nama)) + "| "
        baris += " " * (7 - len(harga)) + harga + " | "
        baris += " " * (5 - len(stok)) + stok
        print(baris)
        no += 1
    print(garis)


def tampilkan_keranjang():
    garis = "-" * 51
    print("No | Nama" + " " * 14 + "|   Harga |  Qty |  Subtotal")
    print(garis)
    no = 1
    for kode in keranjang:
        n = str(no)
        nama = produk[kode]["nama"]
        harga = str(produk[kode]["harga"])
        qty = str(keranjang[kode])
        sub = str(hitung_subtotal(kode))
        baris = n + " " * (3 - len(n)) + "| "
        baris += nama + " " * (18 - len(nama)) + "| "
        baris += " " * (7 - len(harga)) + harga + " | "
        baris += " " * (4 - len(qty)) + qty + " | "
        baris += " " * (9 - len(sub)) + sub
        print(baris)
        no += 1
    print(garis)
    print("TOTAL : Rp", hitung_total_keranjang())


def cetak_struk(bayar, total):
    bersihkan_layar()
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
    print("TOTAL   : Rp", total)
    print("BAYAR   : Rp", bayar)
    print("KEMBALI : Rp", bayar - total)
    print("=" * 40)
    print("   Terima kasih sudah berbelanja!")


def proses_login():
    global user_aktif, program_jalan
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
            print("Username atau password salah! Sisa:", 3 - percobaan)
        else:
            user_aktif = username
            keranjang.clear()
            print("Login berhasil! Selamat datang,", user_aktif)
            return
    print("Login gagal 3x. Program ditutup.")
    program_jalan = False


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
    print("Register berhasil! Silakan login.")


def tambah_produk():
    print("--- TAMBAH PRODUK ---")
    tampilkan_produk()
    print("(ketik 'exit' untuk batal)")
    kode = input_valid("Kode produk : ", cek_kode_baru)
    if kode is None:
        print("\nTambah produk dibatalkan.")
        return
    nama = input_valid("Nama produk : ", cek_nama)
    if nama is None:
        print("\nTambah produk dibatalkan.")
        return
    harga = input_angka("Harga       : ", 1000)
    if harga is None:
        print("\nTambah produk dibatalkan.")
        return
    stok = input_angka("Stok        : ", 0)
    if stok is None:
        print("\nTambah produk dibatalkan.")
        return
    produk[kode] = {"nama": nama, "harga": harga, "stok": stok}
    print("\nProduk berhasil ditambahkan!")


def cek_stok():
    print("--- CEK STOK ---")
    tampilkan_produk()
    print("(ketik 'exit' untuk batal)")
    kode = input_valid("Masukkan kode produk: ", cek_kode_ada)
    if kode is None:
        print("Dibatalkan.")
        return
    stok = produk[kode]["stok"]
    print(produk[kode]["nama"], "-> stok tersisa:", stok)
    if stok == 0:
        print("(Stok HABIS)")
    elif stok <= 5:
        print("(Stok menipis!)")


def ubah_produk():
    print("--- UBAH HARGA / STOK ---")
    tampilkan_produk()
    print("(ketik 'exit' untuk batal)")
    kode = input_valid("Masukkan kode produk: ", cek_kode_ada)
    if kode is None:
        print("\nUbah produk dibatalkan.")
        return
    print("\nProduk :", produk[kode]["nama"])
    print("Harga  :", produk[kode]["harga"])
    print("Stok   :", produk[kode]["stok"])
    print("1. Ubah Harga")
    print("2. Ubah Stok")
    sub = input_valid("Pilih (1/2): ", cek_pilihan_12)
    if sub is None:
        print("\nUbah produk dibatalkan.")
        return
    if sub == "1":
        baru = input_angka("Harga baru: ", 1000)
        if baru is None:
            print("\nUbah produk dibatalkan.")
            return
        produk[kode]["harga"] = baru
        print("\nHarga berhasil diubah!")
    else:
        baru = input_angka("Stok baru: ", 0)
        if baru is None:
            print("\nUbah produk dibatalkan.")
            return
        produk[kode]["stok"] = baru
        print("\nStok berhasil diubah!")


def hapus_produk():
    print("--- HAPUS PRODUK ---")
    if len(produk) == 0:
        print("Belum ada produk.")
        return
    tampilkan_produk()
    print("(ketik 'exit' untuk batal)")
    kode = input_valid("Masukkan kode produk yang dihapus: ", cek_kode_ada)
    if kode is None:
        print("\nPenghapusan dibatalkan.")
        return
    yakin = input("Yakin hapus '" + produk[kode]["nama"] + "'? (y/n): ")
    if yakin.lower() == "y":
        produk.pop(kode)
        print("\nProduk berhasil dihapus!")
    else:
        print("\nPenghapusan dibatalkan.")


def tambah_ke_keranjang():
    print("--- TAMBAH KE KERANJANG ---")
    tampilkan_produk()
    print("(ketik 'exit' untuk batal)")
    kode = input_valid("Kode produk : ", cek_kode_ada_stok)
    if kode is None:
        print("\nDibatalkan.")
        return
    stok = produk[kode]["stok"]
    print("Produk :", produk[kode]["nama"], "(stok tersedia:", stok, ")")
    sudah = keranjang.get(kode, 0)
    if sudah > 0:
        print("(Sudah ada", sudah, "di keranjang)")
    jumlah = input_angka("Jumlah beli : ", 1, stok)
    if jumlah is None:
        print("\nDibatalkan.")
        return
    keranjang[kode] = sudah + jumlah
    produk[kode]["stok"] -= jumlah
    print("\nBarang berhasil masuk keranjang!")


def lihat_keranjang():
    print("--- ISI KERANJANG ---")
    if len(keranjang) == 0:
        print("Keranjang kosong.")
    else:
        tampilkan_keranjang()


def ubah_jumlah_keranjang():
    print("--- UBAH JUMLAH BARANG ---")
    if len(keranjang) == 0:
        print("Keranjang kosong.")
        return
    tampilkan_keranjang()
    daftar = list(keranjang.keys())
    print("(ketik 'exit' untuk batal)")
    nomor = input_angka("Pilih nomor item: ", 1, len(daftar))
    if nomor is None:
        print("\nDibatalkan.")
        return
    kode = daftar[nomor - 1]
    qty_lama = keranjang[kode]
    maks_beli = qty_lama + produk[kode]["stok"]
    qty_baru = input_angka("Jumlah baru (maks " + str(maks_beli) + "): ", 1, maks_beli)
    if qty_baru is None:
        print("\nDibatalkan.")
        return
    produk[kode]["stok"] += qty_lama - qty_baru
    keranjang[kode] = qty_baru
    print("\nJumlah berhasil diubah!")


def batalkan_item():
    print("--- BATALKAN ITEM KERANJANG ---")
    if len(keranjang) == 0:
        print("Keranjang kosong.")
        return
    tampilkan_keranjang()
    daftar = list(keranjang.keys())
    print("(ketik 'exit' untuk batal)")
    nomor = input_angka("Pilih nomor item yang dibatalkan: ", 1, len(daftar))
    if nomor is None:
        print("\nDibatalkan.")
        return
    kode = daftar[nomor - 1]
    produk[kode]["stok"] += keranjang[kode]
    print("\n'" + produk[kode]["nama"] + "' dibatalkan dari keranjang.")
    keranjang.pop(kode)


def bayar_keranjang():
    print("--- PEMBAYARAN ---")
    if len(keranjang) == 0:
        print("Keranjang kosong, tidak ada yang dibayar.")
        return
    tampilkan_keranjang()
    total = hitung_total_keranjang()
    print("(ketik 'exit' untuk batalkan)")
    try:
        bayar = input_angka("Uang bayar : Rp ", total)
        if bayar is None:
            raise InterruptedError("Pembayaran dibatalkan.")
    except InterruptedError as e:
        print("\n" + str(e))
    else:
        cetak_struk(bayar, total)
        keranjang.clear()
    finally:
        print("\n[Proses pembayaran selesai]")


def logout_user():
    global user_aktif
    if len(keranjang) > 0:
        for kode in keranjang:
            produk[kode]["stok"] += keranjang[kode]
        print("Keranjang yang belum dibayar akan dikosongkan.")
    keranjang.clear()
    user_aktif = ""
    print("Logout berhasil.")


def logout_admin():
    global user_aktif
    user_aktif = ""
    print("Logout berhasil.")


def menu_awal():
    global program_jalan
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
        program_jalan = False
    else:
        print("Pilihan tidak valid!")


def menu_admin():
    print("=" * 40)
    print("   MENU ADMIN | Login:", user_aktif)
    print("=" * 40)
    print("1. Tambah Produk")
    print("2. Tampilkan Daftar Produk")
    print("3. Cek Stok Produk")
    print("4. Ubah Harga/Stok Produk")
    print("5. Hapus Produk")
    print("0. Logout")
    pilihan = input_menu()
    if pilihan == "1":
        tambah_produk()
    elif pilihan == "2":
        print("--- DAFTAR PRODUK ---")
        tampilkan_produk()
    elif pilihan == "3":
        cek_stok()
    elif pilihan == "4":
        ubah_produk()
    elif pilihan == "5":
        hapus_produk()
    elif pilihan == "0":
        logout_admin()
    else:
        print("Pilihan tidak valid!")


def menu_user():
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
    pilihan = input_menu()
    if pilihan == "1":
        print("--- DAFTAR PRODUK ---")
        tampilkan_produk()
    elif pilihan == "2":
        cek_stok()
    elif pilihan == "3":
        tambah_ke_keranjang()
    elif pilihan == "4":
        lihat_keranjang()
    elif pilihan == "5":
        ubah_jumlah_keranjang()
    elif pilihan == "6":
        batalkan_item()
    elif pilihan == "7":
        bayar_keranjang()
    elif pilihan == "0":
        logout_user()
    else:
        print("Pilihan tidak valid!")


def main():
    global program_jalan
    while program_jalan:
        bersihkan_layar()
        try:
            if user_aktif == "":
                menu_awal()
            elif users[user_aktif]["role"] == "admin":
                menu_admin()
            else:
                menu_user()
            if program_jalan:
                input("\nTekan Enter untuk lanjut...")
        except (KeyboardInterrupt, EOFError):
            print("\nProgram dihentikan paksa.")
            program_jalan = False


main()