class Hero:
    def __init__(self,name,health,attack_power,armor):
        self.name = name
        self.health = health
        self.attack = attack_power        
        self.armor = armor
        
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attack)
        
    
    def diserang(self, lawan, attack_power_lawan ):
        print(f"{self.name} diserang {lawan.name}")
        attack_diterima = attack_power_lawan/self.armor
        print(f"serangan terasa: {str(attack_diterima)}")
        self.health -= attack_diterima
        print(f"darah : {str(self.health)}")
        
        
sniper = Hero("sniper", 200, 100, 20)
balmond = Hero("balmond", 100, 40, 100)

sniper.serang(balmond)
        
        