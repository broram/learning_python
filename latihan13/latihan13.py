'''disini aku akan membuat semua porgram atau projek 
programer: broram
motifasi: biar asik
'''
import modul.mathutils as prim
import modul.kuis as mkuis
import modul.perpustakan as pp
def main_prim():
    n = int(input("masukan sebuah angka: "))
    result = prim.result_prim(n)
    print(result)
def main_pp():
    data = pp.pemindahan_data()
    while True:
        print("Pilih")
        print("1. Tambah buku")
        print("2. pinjam buku")
        print("3. kembalikan buku")
        print("4. cari buku")
        print("5. keluar")
        pilihan = input("masukan pilihan: ").strip()
        if pilihan == "1":
            pp.tambah_buku(data)
        elif pilihan == "2":
            pp.pinjam_buku(data)
        elif pilihan == "3":
            pp.kembalikan_buku(data)
        elif pilihan == "4":
            pp.cari_buku(data)
        elif pilihan == "5":
            break
        else:
            print("pilihan tidak dikenal")
        

if __name__ ==  "__main__":
    while True :
        print("Pilih Program")
        print("=============")
        print("1. mencari bilangan prima")
        print("2. kuis")
        print("3. Perpustakaan")
        pilihan = int(input("masukan mau program apa : "))
        if pilihan == 1 :
            main_prim()
        elif pilihan == 2 :
            mkuis.kuuis(mkuis.question, mkuis.objek)
        elif pilihan == 3 :
            main_pp()