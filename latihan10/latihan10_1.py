'''tulis catatan ke file'''

with open('tulisfile1.txt', 'w' , encoding="utf8") as bro:
    isi = input('masukan apa aja keta kata: ')
    bro.write(isi)
    
    # print(f"{bro.read()}")
    