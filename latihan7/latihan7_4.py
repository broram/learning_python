'''fungsi nilai maksimum 3 angka'''

def maksimum(a, b, c):
    if a > b and a > c:
       return f"nilai tertinggi adalah {a}"
    elif b > a and b > c:
       return f"nilai tertinggi adalah {b}"
    else:
       return f"nilai tertinggi adalah {c}"
    
print(maksimum(23, 54, 68))