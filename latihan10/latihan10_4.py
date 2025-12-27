'''hitung jumlah baris dalam file'''

with open('D:/ramdan/projek/python/2bulan/filesemua/tulis.txt', 'r') as f:
    i = 0
    for line in f:
        i += 1 

print(i)
    
    