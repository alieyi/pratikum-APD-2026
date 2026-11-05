from data import produk, sesi
from validasi import (
    input_menu, input_angka, input_valid,
    cek_kode_baru, cek_kode_ada, cek_nama, cek_pilihan_12,
)
from tampilan import tampilkan_produk
from stok import cek_stok
from auth import logout_admin


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


def menu_admin():
    print("=" * 40)
    print("   MENU ADMIN | Login:", sesi["user_aktif"])
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
