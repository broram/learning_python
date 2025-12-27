'''mengunakan finaly'''

try:
    def maksimum_nilai(a, b, c):
        if a > b and c:
            return f"nilai tertinggi {a}"
        elif b > a and c:
            return f"nilai tertinggi {b}"
        else:
            return f"niai tertinggi {c}"
    nilai_a = int(input("masukan niali a: "))
    nilai_b = int(input("masukan niali b: "))
    nilai_c = int(input("masukan niali c: "))
except:
    print("masukan input yang bener")
else:
    result = maksimum_nilai(nilai_a, nilai_b, nilai_c)
    print(result)
finally:
    print("program berhasil di jalankan")