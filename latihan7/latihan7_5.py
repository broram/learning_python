'''fungsi penilaian'''

dataNilai = []

# kfungsi grade
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
  
# fugnsi merubah grade menjadi sebuah nama  
def fitur_deskipsi(y):
    if y == "A":
        return "sangat baik"
    if y == "B":
        return "baik"
    if y == "C":
        return "cukup"
    if y == "D":
        return "kurang"
    if y == "E":
        return "sangat kurang"
    
#ini untuk mengubah ke fungsi grade lalu ngirim ke data nilai
def inputan_data():    
    input_nilai = int(input("masukan nilai(1-100): "))
    hasil_grade = grade(input_nilai)
    dataNilai.append(hasil_grade)

if __name__=="__main__":
    while True:
        print("pilih")
        print("1. grade nilai")
        print("2. deksripsi kan nilai")
        pilihan = int(input("masukan nilai : "))
        if pilihan == 1:
            inputan_data()
            print(" ".join(dataNilai)) #join inni untuk menghilangkan tanda list
        elif pilihan == 2:
            for nilai in dataNilai:
                print(f"{nilai} : {fitur_deskipsi(nilai)}")
            
'''Buat fungsi penilaian(nilai) yang mengembalikan grade:

≥ 90: A

≥ 80: B

≥ 70: C

≥ 60: D

< 60: E'''