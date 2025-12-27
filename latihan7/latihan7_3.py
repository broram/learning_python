'''fungsi cek ganjil genap'''


def ganjil_genap(x):
    if x % 2 == 0 :
        return "genap"
    else:
        return "ganjil"
    
x = int(input('masukan angka (cek ganjil genap) : '))
    
print(f"angka {x} adalah angka {ganjil_genap(x)}")