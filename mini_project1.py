'''mananjemen data siswa sederhana'''

mahasiswa = []

def nyimpan_mahasiswa():
    
    nama = input("masukan nama: " )
    nim = input("masukan NIM : ")
    nilai = int(input("masukan nilai : "))
    
    data = {
        "nama" : nama,
        "nim" : nim,
        "nilai" : nilai
    }

    mahasiswa.append(data)

def menampilkan_semua():
    for mhs in mahasiswa:
        print(f"nama : {mhs['nama']} | nim : {mhs['nim']} | nilai : {mhs['nilai']}")
    
def mencari_data():
    nim_cari = input('masukan nim : ')
    ketemu = False
    for mhs in mahasiswa: 
        if nim_cari == mhs["nim"]:
            print(f"nama : {mhs['nama']} | nilai : {mhs['nilai']}")
            ketemu = True
            break
    if not ketemu:
        print("belum dapat")

def menghitung_rata():
    total = 0
    for mhs in mahasiswa:
        total += mhs["nilai"]
    rata = total / len(mahasiswa)
    print(f"rata rata nilai : {rata}")
    
    
while True:
    print("1. tambahkan data mahasiswa")
    print("2. lihat semua data")
    print("3. rata-rata nilai")
    print("4. cari mahasiswa(NIM)")
    print("5. keluar")
    
    pilihan = int(input("pilih : "))
    
    if pilihan == 1:
        nyimpan_mahasiswa()
    elif pilihan == 2:
        menampilkan_semua()
    elif pilihan == 3:
        menghitung_rata()
    elif pilihan == 4:
        mencari_data()
    else:
        break
    
    