'''menghitung jumlah total dari 1 sampai n (while loop)'''
nilaiN = int(input("masukan nilai N(jumlah total sampai n): "))

total = 0
x = 1
while (x <= nilaiN):
    total += x
    x += 1
print("total =", total)

# 1 + 2 + 3 + 4 ... + n