class Hero: 
    
    def __init__(self,name,health,attackpower):
        self.__name = name
        self.__health = health
        self.__attpower = attackpower
        
    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower
        

# awal dari game
ramdan = Hero("Ramdan", 100, 50)
# game berjalan
print(ramdan.getName())
print(ramdan.getHealth())
ramdan.diserang(5)
print(ramdan.getHealth())


        