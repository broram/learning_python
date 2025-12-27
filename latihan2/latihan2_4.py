'''
buat program sederhana yang meminta usia seseorang dan megecek apakah usia tersebut masuk dalam kategori
- anakanak (usia < 12)
- remaja (12 <= usia < 18)
- dewasa (usia >= 18)
'''

usia = int(input("masukan usia kamu: "))

if usia < 12:
    kategori = "anak-anak"
elif 12 <= usia < 18:
    kategori = "remaja"
else:
    kategori = "dewasa"
    
print(f"anda termasuk kategori = {kategori}")