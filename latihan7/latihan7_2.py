'''fungsi konversi suhu'''

def celcius_ke_fahrenheit(cc):
    fahrenheit = (9/5) * cc + 32
    return fahrenheit

cc = int(input("masukan besar suhur(celcius) : "))
print(f"suhu : {celcius_ke_fahrenheit(cc)}f")