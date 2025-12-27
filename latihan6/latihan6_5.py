'''operasi himpunan'''

himp1 = {1, 2, 3, 4}
himp2 = {3, 4, 6,7}

#kita buat fungsinya disinii
def gabungan():
    return himp1 | himp2
def irisan():
    return himp1 & himp2
def selisih():
    return himp1 - himp2

#lalu kita dictionary kan fungsi 
ramdan = {
    "union" : gabungan(),
    "intersection" : irisan(),
    "difverence" : selisih()
}

#dictionary kita loop biar gampang
for key, val in ramdan.items():
    print("%s : %s" % (key, val))
