'''scope: local vs global'''

x = 10

def local(nilai_baru):
    global x
    x = nilai_baru
    
print(x)
local(5)
print(x)