'''program penilaian nilai'''

nilai = int(input("masukan nilai anda: "))

if nilai >= 100:
    print("eror")
elif 90 >= nilai <= 100:
    print("grade A")
elif 80 >= nilai <= 89:
    print("grade B")
elif 70 >= nilai <= 79:
    print("grade C")
elif 60 >= nilai <= 69:
    print("grade D")
else:
    print("grade E")


'''
90-100: A

80-89 : B

70-79 : C

60-69 : D

<60 : E

'''