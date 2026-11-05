from data import produk, keranjang


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
    if len(daftar_kode) == 0:
        return 0
    return hitung_subtotal(daftar_kode[0]) + hitung_total_rekursif(daftar_kode[1:])
