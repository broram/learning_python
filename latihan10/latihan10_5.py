'''cari nama dari di file'''

import os
tetap = 'D:/ramdan/projek/python/2bulan/filesemua/'


# menentukan dimana file yang mau dituju
file = input("masukan nama file: ")
filed = tetap + file +'.txt'

# foder yang mau dituju
filecari = os.path.isfile(filed)

if filecari: #karea os.path itu mengemblikan nilei true
    print("dapat")
else:
    print("tidak dapat")
    

