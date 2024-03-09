class Araba():
    marka=""
    model=""
    renk=""
    durum=""  
    
    #Burada yeni bir terim: Constructor metot , yani en başta nesnelere default olarak özellikler atama işlemi:
    #Bunu sınıfın içinde tanımlamalıyız.
    def __init__(self,marka,model,renk,durum="Çalışmıyor"):  
        self.marka=marka
        self.model=model
        self.renk=renk
        self.durum=durum
        print("Nesne oluşturuldu.")
    
    #Şimdi ise yıkıcı metot yazacağız.
    def __del__(self,):
        print("Nesne silindi")
        
        
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
#Daha kolay nesne oluşturmak için constructor kullanıyoruz.
#Bu aşamada constructor otomatik olarak çalıştığı için hata almamak adına  tüm değerleri parantez içine girmeliyiz.
sedan=Araba("Toyota","Corolla", "Siyah") 

print(f"Markası: {sedan.marka}")
print(f"Modeli: {sedan.model}")
print(f"Rengi: {sedan.renk}")
sedan.durumu_yazdir()
sedan.calistir()
sedan.durumu_yazdir

print("***********************")

sedan.durdur()
sedan.durumu_yazdir()

#Yıkıcı metodu deniyiyoruz.
del sedan