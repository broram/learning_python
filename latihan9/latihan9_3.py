'''tangani banyak jenis eror'''

def pembagian(y):
    return lambda x: x / y

try:
    penyebut = int(input("masukan penyebut: "))
    pembilang = int(input("masukan pembilang: "))
    result = pembagian(penyebut)
    print(result(pembilang))
    
except (ValueError, ZeroDivisionError):
    print("tidak bisa")
    
    
