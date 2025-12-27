'''latihan segitiga angka'''

tinggi_st = int(input("masukan tinggi: "))

for i in range(1, tinggi_st):
    for j in range(1, i + 1):
        print(j,'', end='',sep='')
    print()