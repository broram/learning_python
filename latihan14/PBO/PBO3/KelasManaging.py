class Mahasiswa:
    def __init__(self, name):
        self.__name = name # kita private kan
        
    # getter untuk mengambil nama
    def get_name(self):
        return self.__name 
    

class Kelas:
    def __init__(self, kapasitas):
        self.__kapasitas = kapasitas
        #kita pake list utnuk define ukuran awal
        self.__daftar_mahasiswa = []
        
    def tambah_mahasiswa(self, m):
        #cek apakah jumlah list masih di bawak kapasitas
        if len(self.__daftar_mahasiswa) < self.__kapasitas:
            self.__daftar_mahasiswa.append(m)
        else:
            print("kelas sudah penuh")
            
    def tampilan_daftar(self):
        for m in self.__daftar_mahasiswa:
            # memanggil method get_name dari objek m
            print (m.get.name())
            
            
            
if __name__ == "__main__":
    k = kelas(3) # membuat kapasitas
    
    k.tambah_mahasiswa(Mahasiswa("ali"))
    k.tambah_mahasiswa(Mahasiswa("ramdan"))
    
    k.tampilan.daftar()
    
            
        
        