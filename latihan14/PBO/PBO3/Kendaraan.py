class Kendaraan:
    jumlah_kendaraan = 0 #statik atau class atribut
    
    def __init__(self, model):
        self.model = model # intance atribut 
        Kendaraan.jumlah_kendaraan += 1
        
    def get_model(self):
        return self.model 
    
    @classmethod
    def get_jumlah_kendaraan(cls):
        return cls.jumlah_kendaraan
    
    
    
k1 = Kendaraan("mobil")
k2 = Kendaraan("motor")

print(f"jumalah kendaraan: {Kendaraan.get_jumlah_kendaraan}")
print(f"moddel K1: {k1.get_model()}")
print(f"moddel K2: {k2.get_model()}")
