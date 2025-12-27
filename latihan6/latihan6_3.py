'''menghitung jumlah kata unik'''

ramdan = {
    'aple' : 2,
    'banana' : 4,
    'banana' : 1,
    'orang' : 3,
    'wine' : 5,
    'apple' : 3,
}
menghitung_kata_unik = len(set(ramdan.keys()))
print(f"jumlah kata unik: {menghitung_kata_unik}")