class Hero:
    # private class variabel
    __jumlah = 0
    
    def __init__(self, name, health, attpower, armor):
        self.__name = name
        self.__healthbase = health
        self.__attPowerbase = attpower
        self.__armorbase = armor
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthbase * self.__level
        self.__attPower = self.__attPowerbase * self.__level
        self.__armor = self.__armorbase * self.__level
        
        self.__health = self.__healthMax
        
        Hero.__jumlah += 1
        
    @property
    def info(self):
        return "{} level : \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name, self.__health, self.__healthMax, self.__attPower, self.__armor)
    
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100
            
            self.__healthMax = self.__healthbase * self.__level
            self.__attPower = self.__attPowerbase * self.__level
            self.__armor = self.__armorbase * self.__level
            
    def atttack(self, musuh):
        self.gainExp = 50
            
    
    
ramdan = Hero("ramdan", 100, 50, 50)
putri = Hero("puyy", 100, 30, 30)

print(ramdan.info)

ramdan.atttack(putri)
ramdan.atttack(putri)
ramdan.atttack(putri)

print(ramdan.info)
        
        
        
        