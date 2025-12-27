'''buat error sendiri dengan raise'''
def cek_nilai(n):
    if n >= 90 and n <= 100:
        return "A"
    elif n >= 80 and n <= 100:
        return "B"
    elif n >= 70 and n <= 100:
        return "C"
    elif n >= 60 and n <= 100:
        return "D"
    elif n <= 60 and n > 0:
        return "E"
    else:
        raise ValueError("nilai harus di antara 0-100")

inputan = int(input("masukan nilai: "))    
result = cek_nilai(inputan)
print(result)