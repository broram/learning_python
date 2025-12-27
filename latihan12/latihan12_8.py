'''daftar angka acak'''
import random

data_r = random.randint(10, 100)

result = [x for x in range(data_r) if x % 2 == 0]
print(result)