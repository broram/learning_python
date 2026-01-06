class Rekening:
    def __init__(self, saldo_awal = 0.0):
        # validasi saldo awal
        if saldo_awal >= 0:
            self.__saldo = saldo_awal # gunakan __ untuk "private"
        else:
            print()
            self.__saldo = 0.0
            
    def get_saldo (self):
        print("logging : saldo diakses ")
        return self.__saldo 
    
    def deposit(self, jumlah):
        if jumlah > 0: 
            self.__saldo += jumlah
            print(f"longging: deposit {jumlah} berhasil. saldo baru: {self.__saldo}")
        else:
            print("validasi gagal: jumalh deposit harus lebih dari 0")
            
    def withdraw(self, jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"logging: withdraw {jumlah} berhasil. saldo baru {self.__saldo}")
        else:
            print("validasi gagal: jumlah wihtdraw invalid atau saldo tidak cukup")
            
            

r = Rekening(1000.0)
r.deposit(1000.0)
r.withdraw(200.0)
print(f"saldo akhit: {r.get_saldo()}")

            
                    
        