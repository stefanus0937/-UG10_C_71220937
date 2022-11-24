#Soal 1
print("="*10,"Menu","="*10)
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
print("")
bil1 = int(input("Bilangan 1 : "))
bil2 = int(input("Bilangan 2 : "))
n = int(input("Pilih menu : "))
if n == 1:
    print("hasil:",bil1+bil2)
elif n == 2:
    print("hasil:",bil1-bil2)
elif n == 3:
    print("hasil:",bil1*bil2)
elif n == 4:
    print("hasil:",float(bil1//bil2))
else:
    print("INVALID!!")
    print("Try Again")
