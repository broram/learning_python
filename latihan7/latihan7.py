'''fungsi konversi suhu'''

def celcius_ke_fahrenheit():
    cc = int(input("masukan besar suhur(celcius) : "))
    fahrenheit = (9/5) * cc + 32
    return fahrenheit

print(f"suhu : {celcius_ke_fahrenheit()}f")