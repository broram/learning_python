'''buat list ganjil kuadrat'''
list = list(range(1, 21))
kdrt_ganjil = [i**2 for i in list if i % 2 == 1]
print(kdrt_ganjil)