class Pegawai:
    def __init__(self, name, umur):
        self.name = name # this = self dalam python 
        self.umur = umur
    
    def update_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name


ramdan = Pegawai("ramdan", 12)
print(ramdan.get_name())
ramdan.update_name("ramdan hebat")
print(ramdan.get_name())