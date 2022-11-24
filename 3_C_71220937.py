#soal 3
daftar = input("Masukan daftar pesanan : ")
hasil1 = daftar.title()
print("Daftar Pesanan :",hasil1.split(","))
tambahan = input("Masukkan pesanan yang ingin ditambahkan : ")
if tambahan in daftar:
    print(tambahan.upper(),"sudah berada dalam daftar pesanan")
else:
    hasil2 = daftar.title(),tambahan
    print("Hasil penambahan pada daftar pesanan :",hasil2)
