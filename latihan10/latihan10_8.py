'''ubah kta di file'''

with open('D:/ramdan/projek/python/2bulan/filesemua/tulis.txt', 'r') as aw:
    fileaw = aw.read()
    
ramdan = fileaw.replace("Padang", "bukittinggi")

with open('D:/ramdan/projek/python/2bulan/filesemua/lol.txt', 'w') as wokW:
    wokW.write(ramdan)