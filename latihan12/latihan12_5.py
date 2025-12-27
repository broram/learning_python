'''hapus semua file'''
import os
file = r"D:\ramdan\projek\python\2bulan\latihan12\modul"

with os.scandir(file) as ow:
    for i in ow:
        if i.is_file() and i.name.endswith('.txt') and "1" in i.name:
            pilihan = input("yakin haput file?, y/n : ")
            if pilihan.lower() == "y":
                os.remove(i.path)
                print(f"file berhasil dihapus {i.name}")
            else:
                print(f"file tidak dihapus{i.name}")
            