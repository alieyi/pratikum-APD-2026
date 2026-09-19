barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000

barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]
total_belanja = (barang[0] + barang[1] + barang[2] + barang[3] + barang[4] + barang[5])
pajak = total_belanja * 0.15
total_bayar = total_belanja + pajak


rata_rata = total_bayar / len(barang)
nim = 13
bolean = nim < rata_rata

total_euro = total_bayar / 20455
total_yuan = total_bayar / 2659


print("isi variabel barang:", barang)
print("total belanja:", total_belanja)
print("pajak:", pajak)
print("total bayar:", total_bayar)
print("total euro:", total_euro)
print("total yuan:", total_yuan)
print("rata-rata:", rata_rata)
print("NIM:", nim)
print("boolean:", bolean)
print("barang slicing:", barang[0], barang[2], barang[4])