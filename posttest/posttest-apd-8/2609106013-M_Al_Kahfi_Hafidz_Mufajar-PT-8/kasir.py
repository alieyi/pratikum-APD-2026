from data import produk, keranjang, sesi
from validasi import input_menu, input_angka, input_valid, cek_kode_ada_stok
from perhitungan import hitung_total_keranjang
from tampilan import tampilkan_produk, tampilkan_keranjang, cetak_struk
from stok import cek_stok
from auth import logout_user


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


def menu_user():
    print("=" * 40)
    print("   MENU PENGGUNA | Login:", sesi["user_aktif"])
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
