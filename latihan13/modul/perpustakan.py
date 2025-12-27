import json
import os

Buku_PATH = "D:\\ramdan\\projek\\python\\2bulan\\latihan13\\modul\\buku.json"

def pemindahan_data():
    try:
        with open(Buku_PATH, 'r') as file:
            return ('ada')
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        return ("file ada tapi json rusak: ", e)
        return []
    except Exception as e:
        return ("error saat baca file: ",e)
        return []

def save_data(data):
    try:
        # pastikan forder ada
        forder = os.path.dirname(Buku_PATH)
        os.makedirs(forder, exist_ok = True)
        with open (Buku_PATH, "w") as f:
            json.dump(data, f, ensure_ascii = False, indent=4)
            return True
    except Exception as e:
        return (f"error saat menyimpan data: {e}") #menampilkan eror
        return False

def tambah_buku(data):
    
    judul = input("masukan judul buku : ")
    penulis = input("masukan penulis buku : ")
    tahun = int(input("masukan tahun : "))
    stok = int(input("masukan stok : "))
    
    entry = {
        "judul" : judul,
        "penulis" : penulis,
        "tahun" : tahun,
        "stok" : stok
    }
    
    if not isinstance(data, list):
        data = []
        
    data.append(entry)
    
    if save_data(data): #panggilan untuk save_data
        return ("buku berhasil dimasukan")
    else:
        return ("gagal menyimpan buku")
        
def pinjam_buku(data):
    inputb = input("masukan nama buku: ")
    
    buku_ditemukan = False
    
    for buku in data:
        if buku['judul'].lower() == inputb.lower():
            buku['stok'] -= 1
            save_data(data)
            return ("buku berhasil di pinjam")
            buku_ditemukan = True
            break
    
    if not buku_ditemukan:
        return ("buku tidak ditemukan")    
    
def kembalikan_buku(data):
    inputb = input("masukan nama buku: ")
    
    buku_ditemukan = False
    
    for buku in data:
        if buku['judul'].lower() == inputb.lower():
            buku['stok'] += 1
            save_data(data)
            return ("buku berhasil di kembalikan")
            buku_ditemukan = True
            break
    
    if not buku_ditemukan:
        return ("buku tidak ditemukan")
            
def cari_buku(data):
    nama_buku = input("masukan buku apa yang mau dicari: ")
    hasil = [buku for buku in data if nama_buku.lower() in buku["judul"].lower()]
    if hasil: 
        return ("\nhasi pencarian ditemukan: ")
        for buku in hasil: 
            return (f"judul: {buku['judul']}, stok : {buku.get('stok')}, tahun: {buku.get('tahun')}")
    
    else:
        return ("buku tidak ditemukan") 
    

    

