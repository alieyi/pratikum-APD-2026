import os
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore
from data import produk, keranjang, sesi
from perhitungan import hitung_subtotal, hitung_total_keranjang


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_produk():
    if len(produk) == 0:
        print("Belum ada produk.")
        return
    tabel = PrettyTable()
    tabel.field_names = ["No", "Kode", "Nama", "Harga", "Stok"]
    no = 1
    for kode in produk:
        tabel.add_row([
            no,
            kode,
            produk[kode]["nama"],
            produk[kode]["harga"],
            produk[kode]["stok"],
        ])
        no += 1
    tabel.align["Nama"] = "l"
    tabel.align["Harga"] = "r"
    tabel.align["Stok"] = "r"
    print(Fore.BLUE + str(tabel))


def tampilkan_keranjang():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Harga", "Qty", "Subtotal"]
    no = 1
    for kode in keranjang:
        tabel.add_row([
            no,
            produk[kode]["nama"],
            produk[kode]["harga"],
            keranjang[kode],
            hitung_subtotal(kode),
        ])
        no += 1
    tabel.align["Nama"] = "l"
    tabel.align["Harga"] = "r"
    tabel.align["Qty"] = "r"
    tabel.align["Subtotal"] = "r"
    print(Fore.BLUE + str(tabel))
    print("TOTAL : Rp", hitung_total_keranjang())


def cetak_struk(bayar, total):
    bersihkan_layar()
    waktu = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("=" * 40)
    print("        STRUK PEMBELIAN")
    print("        MINIMARKET")
    print("=" * 40)
    print("Kasir   :", sesi["user_aktif"])
    print("Tanggal :", waktu)
    tabel = PrettyTable()
    tabel.field_names = ["Barang", "Qty", "Harga", "Subtotal"]
    for kode in keranjang:
        qty = keranjang[kode]
        harga = produk[kode]["harga"]
        tabel.add_row([produk[kode]["nama"], qty, harga, qty * harga])
    tabel.align["Barang"] = "l"
    tabel.align["Qty"] = "r"
    tabel.align["Harga"] = "r"
    tabel.align["Subtotal"] = "r"
    print(tabel)
    print("TOTAL   : Rp", total)
    print("BAYAR   : Rp", bayar)
    print("KEMBALI : Rp", bayar - total)
    print("=" * 40)
    print("   Terima kasih sudah berbelanja!")
