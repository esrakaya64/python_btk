class Araba():
    marka=""
    model=""
    renk=""
    durum=""  
    
    
    def marka_atama(self, marka):
        self.marka=marka
    
    def model_atama(self,model):
        self.model=model
    
    def renk_atama(self,renk):
        self.renk=renk
        
    def durum_atama(self,durum):
        self.durum=durum
    
    def calistir(self):
        self.durum="Çalışıyor"
    
    def durdur(self):
        self.durum="Çalışmıyor"
    
    def durumu_yazdir(self):
        print(f"Durumu:{self.durum}")
    
#-----------------------------

sedan=Araba()
sedan.marka_atama("Toyota")
print(f"Markası: {sedan.marka}")
sedan.model_atama("Corolla")
print(f"Modeli: {sedan.model}")
sedan.renk_atama("Beyaz")
print(f"Rengi: {sedan.renk}")
sedan.durumu_yazdir()
sedan.calistir()
sedan.durumu_yazdir
print("***********************")
sedan.durdur()
sedan.durumu_yazdir()



