class Yayinlar():
    def __init__(self, isbn, yayinAdi, basimTarihi):
        self.isbn = isbn
        self.yayinAdi= yayinAdi
        self.basimTarihi = basimTarihi
        
    def Yazdir(self):
        print(f"ISBN: {self.isbn} \nYayın Adı: {self.yayinAdi} \nBasım Tarihi: {self.basimTarihi}") 
        
    def GetIsbn(self):
        print(self.isbn)
        
    def SetIsbn(self, yeniIsbn):
        self.isbn=yeniIsbn
    
class Kitaplar(Yayinlar): 
    def __init__(self, isbn,yayinAdi, basimTarihi, yazar, yayinEvi, kitaplikYeri):
        self.yazar=yazar
        self.yayinEvi=yayinEvi
        self.kitaplikYeri=kitaplikYeri
        super().__init__(isbn, yayinAdi, basimTarihi)
        
    def Yazdir(self):
        super().Yazdir()
        print(f"Yazar: {self.yazar}\nYayın Evi: {self.yayinEvi}\nKitaplık Yeri: {self.kitaplikYeri}")   
        
class SureliYayinlar(Yayinlar):
    def  __init__(self, isbn, yayinAdi, basimTarihi, alan, sayi, dergilikYeri):
        self.alan=alan
        self.sayi=sayi
        self.dergilikYeri=dergilikYeri
        super().__init__(isbn, yayinAdi, basimTarihi)

    def YazdirSY(self):
        super().Yazdir()
        print(f"Alan:\t{self.alan}\nSayısı:\t{self.sayi} \nDergilik Yeri:\t{self.dergilikYeri}")
    


# Testler
b1 = Kitaplar("062513487X", "Masumiyet Müzesi", "1990", "Orhan Pamuk", "Aras Yayinciliği", "Türk Klasikleri")
b1.Yazdir()

print("*******************")

s1=SureliYayinlar("9781481979763","Modern Fizik", "2010", "Erhan Pesen", "1000", "Bilim")
s1.YazdirSY()