'''function pengambilan function'''

def kali(y):
    return lambda x: x * y

pengali5 = kali(5)
print(pengali5(3))