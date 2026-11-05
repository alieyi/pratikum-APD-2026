from colorama import Fore
from data import produk
from validasi import input_valid, cek_kode_ada
from tampilan import tampilkan_produk


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
        print(Fore.RED + "(Stok HABIS)")
    elif stok <= 5:
        print(Fore.YELLOW + "(Stok menipis!)")
