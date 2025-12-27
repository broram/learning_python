'''inputan harus angka'''

# kfungsi grade
try:
    def grade(x):
        if x > 100: 
            return "kelebihan hasil"
        elif x >= 90:
            return "A"
        elif x >= 80:
            return "B"
        elif x >= 70:
            return "C"
        elif x >= 60:
            return "D"
        else:
            return "E"
        
    intgra = int(input("masukan nilai: "))
    result = grade(intgra)

    print(result)
except ValueError:
    print("masukan angka lol")