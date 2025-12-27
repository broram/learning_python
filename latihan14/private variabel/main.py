class Hero:
    jumlah = 0
    __private_jumlah = 0
    
    def __init__(self,name,love):
         self.name = name
         self.love = love
         
        # private variabel
         self.__private = "sange"
        # protected variabel
         self._protected = "cemburu"
        
        
ramdan = Hero("ramdan", 100)
putri = Hero("putri", 200)

print(ramdan.__dict__)
print(putri.__dict__)
print(Hero.__private_jumlah)                  
          