'''tangani error pembagian nol'''

try:
    def perkalian(y):
        return lambda x: x / y

    pembilang = int(input("masukan angka 1:"))
    penyebut = int(input("masukan angka 2:"))

    inputanpembilang = perkalian(penyebut)
    print(inputanpembilang(pembilang))
    
except ZeroDivisionError:
    print("untuk masukan angka2 jangan nol KOCAK!!")