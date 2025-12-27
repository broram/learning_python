'''baca dan tambpilkan file'''
try:
    with open('D:/ramdan/projek/python/tulisfile1.txt', 'r') as f:
        for x in f:
            print(x)
except FileNotFoundError:
    print('file tidak kebaca')
    