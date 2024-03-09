class Hayvan():
    
    #Önce attribute yani özelliklerini tanımlıyoruz. Şimdilik boş olarak tanımlıyoruz.
    ad=""
    renk=""
    ayakSayisi=0
    cins=""
    
    #Ardından methodları tanımlıyoruz.
    #Oluşturulan her metotda ilk olarak self tanımlanmalıdır. Burada self, yaratılan nesneyi temsil eder.
    def Ses(self, sesi):
        print(f"{self.ad} hayvanının çıkardığı ses {sesi} dir")
        
#Hayvan sınıfıdndan bir nesne oluşturalım. 
kopek=Hayvan()

#Köpek nesnesinin özelliklerini tanımlayalım.
kopek.ad= "Buddy"
kopek.renk="Beyaz"
kopek.ayakSayisi =4
kopek.cins ="Doberman"

#Denemek için adını yazdıralım.
print("Ad: ", kopek.ad)

#Şimdi köpeğe ait metotları düzenliyoruz.
kopek.Ses("Hav hav")
