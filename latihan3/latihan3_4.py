''' Cek Angka Ganjil/Genap & Positif/Negatif'''

# masukan input
angka = int(input('masukan angka: '))

# cara kerja
if angka >= 0:
    if (angka % 2) == 0:
        print("angka bilangan positif genap")
    else:
        print("angka bilangan positif ganjil")
else:
    if (angka % 2) == 0:
        print("angka bilangan negatif genap")
    else:
        print("angka bilangan negatif ganjil")