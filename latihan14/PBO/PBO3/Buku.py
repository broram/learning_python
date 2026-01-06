class Buku:
    def __init__(self, judul = "ramdan", tahun = 2021):
        self.judul = judul 
        self.tahun = tahun
        
    def get_info(self):
        return f"{self.judul} ({self.tahun})"
    
    
    
b1 = Buku()
b2 = Buku("putri", 2023)
print(b1.get_info())
print(b2.get_info())
        