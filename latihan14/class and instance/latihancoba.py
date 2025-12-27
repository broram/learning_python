class Hero:
    #class variabel 
    jumlah = 0
    
    def __init__(self, inputNama, inputHealth, inputPower, inputArmor):
        #instance variabel 
        self.name = inputNama
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print(f"membuar hero dengan nama {inputNama}")


hero1 = Hero("sniper", 100, 50, 20)
print(Hero.jumlah)
hero2 = Hero("boboiboy", 200, 100, 30)
print(Hero.jumlah)
hero3 = Hero("udin", 1000, 10, 1000)
print(Hero.jumlah)
        
        
        
