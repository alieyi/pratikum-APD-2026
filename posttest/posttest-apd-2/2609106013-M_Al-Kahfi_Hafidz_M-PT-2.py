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
total_euro = total_bayar / 20455
total_yuan = total_bayar / 2659

rata_rata = total_bayar / len(barang)

nim = 13
bolean = nim < rata_rata

print(barang)
print(total_belanja)
print(pajak)
print(total_bayar)
print(total_euro)
print(total_yuan)
print(rata_rata)
print(nim)
print(bolean)
print(barang[0], barang[2], barang[4])