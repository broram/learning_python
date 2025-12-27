''' cek file ada atau tidak'''
try: 
    disini = input("masukan letak file: ")
    with open('D:/ramdan/projek/python/bukuaArisDefiana/140625/'+ disini +'.txt', 'r') as file:
        konten = file.read()
        print(konten)
except FileNotFoundError:
    print('ngga ada bro')