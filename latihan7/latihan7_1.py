'''fungsi luas persegi panjanh'''

def fungsi_luasPP(p, t):
    hasil = p * t
    return hasil

panjang = int(input('masukan panjang : '))
tinggi = int(input('masukan tinggi : '))

print(f"luas persegi panjangnya adalah {fungsi_luasPP(panjang, tinggi)}")