'''Mini Game Sederhana - Tebak Angka'''
# import packages random
import random

nilai = int(input("tebak angka 1-5 : "))
angkaAcak = random.randint(1,5)

if angkaAcak == nilai:
    print("tebakan anda benar")
else:
    print("tebakan salah")
    if angkaAcak >= nilai:
        print("tebakan anda telalu besar")
    else :
        print("tebakan anda terlalu kecil")