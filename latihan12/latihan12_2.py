'''simulasi dadu'''
import random
acak_data = []
n = 1
while n < 10:
    data = random.randint(1, 6)
    acak_data.append(data)
    n += 1

print(acak_data)