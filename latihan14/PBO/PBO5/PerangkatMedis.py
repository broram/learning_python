class PerangkatMendis:
    def __init__(self, nama):
        if nama and nama.strip():
            self.__nama = nama
        else:
            print("Nama invalid, set default 'perangkat'")
            self.__nama = "Perangkat"
            
    def get_nama(self):
        return self.__nama
    
    def aktifkan(self):
        print(f"aktifkan perangkat mendis{self.__nama}")
    
    def hitung_data(self):
        return 0.0
    
class Thermometer(PerangkatMendis):
    def __init__(self, nama, suhu_awal):
        super().__init__(nama)        
        self.__sensor_suhu = float(suhu_awal)
    
    def aktifkan(self):
        super().aktifkan() # panggil logika dasar
        if self.__sensor_suhu > 37.0:
            print(f"warning: suhu tinggil. suhu{self.__sensor_suhu}")
        else:
            print(f"suhu normal: {self.__sensor_suhu}")
            
    def hitung_data(self):
        return self.__sensor_suhu
    
    
if __name__ == "__main__":
    # skenario suhu tinggi
    print("--- Test 1: suhu tinggi ---")
    th1 = Thermometer("ThermoGun", 38.5)
    th1.aktifkan()
    print(f"data suhu: {th1.hitung_data()}")
    
    print("\n--- Test 2: Nama Invalid & Suhu Normal ---")
    # skenario 2: Nama Kosong & suhu normal
    th2 = Thermometer("", 36.5)
    th2.aktifkan()