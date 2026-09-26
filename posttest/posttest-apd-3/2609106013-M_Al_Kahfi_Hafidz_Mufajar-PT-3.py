nama = input("Masukkan Nama Anda : ")
umur = int(input("Masukkan Umur Anda : "))

if umur < 13 :
    print ("Maaf Umur Anda Belum Cukup Untuk Menonton")
else :
    jenis_tiket = input("Pilih Jenis Tiket (reguler/premium/vip) : ")
    if jenis_tiket == "reguler":
        harga_tiket = 50000
        status_member = input("Apakah Anda Memiliki Member (ya/tidak) : ")
        nominal_diskon = harga_tiket * (20/100) if status_member == "ya" else 0
        biaya_admin = 0 if status_member == "ya" else 2000
        total_bayar = harga_tiket - nominal_diskon + biaya_admin
        nominal_uang_bayar = int(input("Masukkan Nominal Uang Anda : "))
        if nominal_uang_bayar < total_bayar:
            print("Uang yang dibayarkan Tidak Cukup")
        else :
            kembalian = nominal_uang_bayar - total_bayar
            print("                      ")
            print(" STRUK PEMBELIAN TIKET")
            print(" ======================")
            print(" Nama         :",nama)
            print(" Umur         :",umur)
            print(" Jenis Tiket  :",jenis_tiket)
            print(" Status Member:",status_member)
            print(" Total Bayar  :",total_bayar)
            print(" Kembalian    :",kembalian)
    elif jenis_tiket == "premium":
        harga_tiket = 75000
        status_member = input("Apakah Anda Memiliki Member (ya/tidak) : ")
        nominal_diskon = harga_tiket * (20/100) if status_member == "ya" else 0
        biaya_admin = 0 if status_member == "ya" else 2000
        total_bayar = harga_tiket - nominal_diskon + biaya_admin
        nominal_uang_bayar = int(input("Masukkan Nominal Uang Anda : "))
        if nominal_uang_bayar < total_bayar:
            print("Uang yang dibayarkan Tidak Cukup")
        else :
            kembalian = nominal_uang_bayar - total_bayar
            print("                      ")
            print(" STRUK PEMBELIAN TIKET")
            print(" ======================")
            print(" Nama         :",nama)
            print(" Umur         :",umur)
            print(" Jenis Tiket  :",jenis_tiket)
            print(" Status Member:",status_member)
            print(" Total Bayar  :",total_bayar)
            print(" Kembalian    :",kembalian)
    elif jenis_tiket == "vip":
        harga_tiket = 100000
        status_member = input("Apakah Anda Memiliki Member (ya/tidak) : ")
        nominal_diskon = harga_tiket * (20/100) if status_member == "ya" else 0
        biaya_admin = 0 if status_member == "ya" else 2000
        total_bayar = harga_tiket - nominal_diskon + biaya_admin
        nominal_uang_bayar = int(input("Masukkan Nominal Uang Anda : "))
        if nominal_uang_bayar < total_bayar:
            print("Uang yang dibayarkan Tidak Cukup")
        else :
            kembalian = nominal_uang_bayar - total_bayar
            print("                      ")
            print(" STRUK PEMBELIAN TIKET")
            print(" ======================")
            print(" Nama         :",nama)
            print(" Umur         :",umur)
            print(" Jenis Tiket  :",jenis_tiket)
            print(" Status Member:",status_member)
            print(" Total Bayar  :",total_bayar)
            print(" Kembalian    :",kembalian)
    else :
        print("Jenis Tiket Yang dipilih Tidak Ada") 
