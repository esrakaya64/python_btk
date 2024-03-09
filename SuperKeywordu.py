class Personel():
    def __init__(self,ad,soyad,kimlikNo):
        self.ad=ad
        self.soyad=soyad
        self.kimlikNo=kimlikNo
        
    def bilgileriYaz(self):
        print(f"Adı Soyadı: {self.ad}  \nSoyadı: {self.soyad}  \nKimlik Numarası: {self.kimlikNo}")
        

class Ogrenci(Personel):
    ogrenciNo="Belirtilmemiş"
    
    def __init__(self,ad,soyad,kimlikNo,ogrenciNo):#Üst sınıftaki init fonskiyonunun parametrelerini de  mutlaka almalı.
        self.ogrenciNo = ogrenciNo
        super().__init__(ad, soyad, kimlikNo)#ve süper class(üst sınıfın) parametrelerini bu lekilde tanımçıyoruz.
        print("Öğrenci kaydedildi.")
        
    def OgrenciNoDegistir(self, yeniOgrenciNo):
        self.ogrenciNo=yeniOgrenciNo
        
kaan=Ogrenci("Kaan", "Somuncu", 1234567891,123)
kaan.bilgileriYaz()#Burada outputa dikkat edersek, önce alt sınıfın init metodu çalışıyor ve sonrasında üst sınıftaki işlemler yapılıyor.