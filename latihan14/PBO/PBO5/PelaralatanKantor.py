class PeralatanKantor:
    def __init__(self, nama):
        self.__nama = nama if nama else "Peralatan"
    
    def gunakan(self):
        print(f"gunakan peralatan kantor: {self.__nama}")
        
    def hitung_biaya(self):
        return 0.0
    
class Printer(PeralatanKantor):
    def __init__(self, nama, tinta_awal):
        super().__init__(nama) # panggil konstruktor superclass
        self.__tinta = tinta_awal if tinta_awal >= 0 else 100
        
    def gunakan(self):
        super().gunakan()
        if self.__tinta > 10:
            print("printer mencetak, tinta berkurang")
            self.__tinta -= 10
        else: 
            print("tinta rendah, tidak bisa dicetak")
            
    def get_tinta(self):
        return self.__tinta
    

pr = Printer("laser printer", 50)
pr.gunakan()
print("tinta sisa: ", pr.get_tinta())
pr.gunakan()
print("tinta sisa: ", pr.get_tinta())