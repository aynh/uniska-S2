print("Program Menghitung Luas")
print("***********************")
print("Pilih menu")
print("=====> 1. Luas lingkaran")
print("       2. Luas persegi panjang")
print("       3. Luas segitiga")

pilihan = int(input("Pilih: "))

print()
if pilihan == 1:
    print("Program lingkaran")
    print("*****************")

    radius = int(input("Masukkan jari-jari: "))

    luas = 3.14 * radius * radius

    print("Luas lingkaran =", luas)
elif pilihan == 2:
    print("Program persegi Panjang")
    print("***********************")

    panjang = int(input("Masukkan panjang: "))
    lebar = int(input("Masukkan lebar: "))

    luas = panjang * lebar

    print("Luas persegi panjang =", luas)
elif pilihan == 3:
    print("Program segitiga")
    print("****************")

    alas = int(input("Masukkan alas: "))
    tinggi = int(input("Masukkan tinggi: "))

    luas = 0.5 * alas * tinggi

    print("Luas segitiga =", luas)
else:
    print("Pilihan menu tidak ada")
