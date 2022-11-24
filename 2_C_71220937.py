#soal 2
b = int(input("Masukan bulan (1-12): "))
if b == 2:
    print("jumlah Hari: 28")
elif b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
    print("jumlah Hari: 31")
elif b == 4 or b == 6 or b == 9 or b == 11:
    print("jumlah Hari: 30")
else:
    print("Invalid")
