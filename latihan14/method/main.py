class Hero:
    #variabel class
    jumlah = 0
    
    def __init__(self, inputName, inputPower, inputHealth, inputArmor):
        # instance variabel
        self.name = inputName
        self.Power = inputPower
        self.health = inputHealth
        self.armor = inputArmor
        Hero.jumlah += 1
        
    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print(f"nama ku adalah {self.name}")
        
    # method dengan argument tanpa return
    def tambahHealth(self, up):
        self.health += up
        
    # method dengan return
    def getHealth(self):
        return self.health
        
        
hero1 = Hero("ramdan", 90, 90, 90)
hero2 = Hero("udin", 100, 50, 100)

hero2.siapa()
hero2.tambahHealth(10)
print(hero2.getHealth())


        
        