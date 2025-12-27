'''gabungkan dua file'''

def gabung_file(file1, file2, filegabung):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(filegabung, 'w') as fout:
            fout.write(f1.read())
            fout.write("\n")
            fout.write(f2.read())
    except FileExistsError:
        print("salah satu file tidak ditemukan")
    except Exception as e:
        print(f"terjadi kesalahan {e}")
        
x = input('masukan file pertama yang mau digabungkan : ')
y = input('masukan file kedua yang mau digabungkan : ')
xy = input('nama file yang digabung : ')

        
pathfile1 = 'D:/ramdan/projek/python/2bulan/filesemua/'+ x +'.txt'
pathfile2 = 'D:/ramdan/projek/python/2bulan/filesemua/'+ y +'.txt'
pathgabung= 'D:/ramdan/projek/python/2bulan/filesemua/'+ xy +'.txt'

gabung_file(pathfile1, pathfile2, pathgabung)

