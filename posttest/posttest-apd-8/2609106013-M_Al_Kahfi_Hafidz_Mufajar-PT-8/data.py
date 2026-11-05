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

sesi = {"user_aktif": "", "program_jalan": True}

HURUF = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ANGKA = set("0123456789")
