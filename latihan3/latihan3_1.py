'''program ini mengecek bilangan positif negatif dan nol'''

x = int(input("masukan sebuah angka: "))

if x < 0:
    print('angka tersebuat adalah bilangan negatif')
elif x > 0:
    print('angka tersebut adalah bilangan positf')
else:
    print('bernilai 0')