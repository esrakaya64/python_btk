class Kisi():
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim
    def ismi_ver(self):
        print(self.isim)
        
class Calisan(Kisi):
    def __init__(self, isim, soyisim, calisan_id, maas):
        self.calisan_id=calisan_id
        self.__maas=maas
        super().__init__(isim, soyisim)
        
    def MaasAyarla(self, yeniMaas):
        if self.__class__== Calisan:
            print(self.__maas)
        else:
            print("Böyle bir yetkiniz bulunmamakta..")
    def GetMaas(self):
        if self.__class__== Calisan:
            print(self.__maas)
        else:
            print("Böyle bir yetkiniz bulunmamakta..")
    
    def PersonelBilgileriniVer(self):
        print(f"Çalışanın adı soyadı: {self.isim} {self.soyisim} \n Çalışan id: {self.calisan_id} \nÇalışanın maaşı: {self.GetMaas()}")
        
class Yonetici(Calisan):
    def __init__(self, isim, soyisim, calisan_id, maas, departman, bagli_calisanlar):
        self.departman= departman
        self.bagli_calisanlar= bagli_calisanlar
        super().__init__(isim,soyisim,calisan_id, maas)  
                         
    def bagliCalisanEkle(self, yeniBagliCalisan):
        self.bagli_calisanlar.append(yeniBagliCalisan) 
    def  bagliCalisanlariListele(self):
        for i in range(len(self.bagli_calisanlar)):
            print(f"{i+1}. {self.bagli_calisanlar[i].isim} {self.bagli_calisanlar[i].soyisim}")     
            
# Testler
calisan1= Calisan("Ozan","Alptekin",101, 30000)
calisan2= Calisan("Toprak", "Alptekin", 102, 40000)
yonetici1=Yonetici("Ahmet", "Mehmet", 201, 75000, "Yönetim", [calisan1])
print("-----GüncelHali-----")
yonetici1.bagliCalisanlariListele()   
yonetici1.bagliCalisanEkle(calisan2)
print("-----GüncelHali-----")
yonetici1.bagliCalisanlariListele()      
print("-----GüncelHali-----")
yonetici1.PersonelBilgileriniVer()
print("-----GüncelHali-----")
calisan1.GetMaas()
