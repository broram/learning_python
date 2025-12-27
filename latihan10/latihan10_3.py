'''simpan daftar nama'''

file = input("masukan tempat file: ")

with open('D:/ramdan/projek/python/2bulan/filesemua/'+ file +'.txt', 'a') as f:
    while True:
        nama = input("masukan nama (e untuk keluar): ")
        if nama == "e": 
            break
        f.write(nama + '\n')