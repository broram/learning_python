class Mahasiswa:
    # variabel milik smua objek 
    jumlah_Mahasiswa = 0
    
    def __init__(self, name, nilai = None):
        self.name = name 
        if nilai is None:
            self.nilai = []
        else:
            self.nilai = nilai 
    
    def hitung_rata_rata(self):
        if len(self.nilai) == 0:
            return 0.0 # handle array kosong 
        
        total = 0 
        for n in self.nilai:
            total += n
        
        return total/ len(self.nilai)
    
    def tambah_nilai(self, nilai_baru):
        self.nilai.append(nilai_baru)
        return self # untuk method chaining 
    
    def get_name(self):
        return self.name 
    
    def get_nilai(self):
        return self.nilai
    
ramdan = Mahasiswa("ramdan", [90,20,30])
print(f"nama: {ramdan.get_name()}")
print(f"nama: {ramdan.get_nilai()}")
print(f"nama: {ramdan.hitung_rata_rata()}")
    