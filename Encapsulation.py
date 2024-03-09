#Erişim belirleyicilerden private olanını kullanarak özel bir hale getirebiliriz. 
#Pythonda private olduğunu belirtmek için alt çizgi (_) kullanılır.
class Ogrenci():
    def __init__(self, no, adSoyad, tcKimlik):
        self.no=no
        self.adSoyad = adSoyad
        self.__tcKimlik = tcKimlik #tc kimlik numarasının private yaptık
        
    #Bu özel bilgilerin erişimine izin vermek için bir method yazıyoruz.
    def get_tc(self, sifre):
        if sifre==1234:
            print(self.__tcKimlik)
        else:#Yanlış şifre girilirse tc sansürlenir
            print("******")
        
    def  set_tc(self, yeniTc, sifre):
        if sifre==1234:
            self.__tcKimlik=yeniTc
        else:
            print("Giriş başarısız! Lütfen doğru şifreyi girin.")
esra=Ogrenci(1,"Esra Yıldız", "1234567890")
print(esra.no)
print(esra.adSoyad)
#print(esra.tcKimlik) #Çalışmaz hata verir çünkü tc kimlik sadece kendi sınıfından erişilebilecek şekilde private yapılmıştır.
esra.get_tc(1234)#Şifreyi girdik.

print("----------------")
esra.set_tc(34354353, 1234)#Doğru şifreyi girdik ve tcyi değiştirmesini bekliyoruz.
esra.get_tc(1234)#Deneyelim.