from colorama import Fore
from data import produk, users, HURUF, ANGKA


def input_menu():
    """Mengambil pilihan menu dari user."""
    pilihan = input("Pilih menu: ").strip()
    print()
    return pilihan


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
        print(Fore.RED + "Error: " + pesan_error)
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
        print(Fore.RED + "Error: " + str(e))
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
