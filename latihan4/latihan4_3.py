'''minta user input sampe benar'''

# import packages random
import random

# batas bawah
a = int(input("masukan batas bawah: "))
# batas atas
b = int(input("masukan batas atas: "))
angkaAcak = random.randint(a,b)

while True:
    nilai = int(input(f"tebak angka ({a}-{b}) : "))
    if angkaAcak == nilai:
        print("tebakan anda benar")
        break
    else:
        print("tebakan salah")
        if nilai >= angkaAcak :
            print("tebakan anda telalu besar")
        else :
            print("tebakan anda terlalu kecil")
            