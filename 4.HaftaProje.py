import sqlite3 as sql
from ui import UI
vt = sql.connect("/Users/esrakaya/Desktop/Btk Python/kutuphane.db")#Böyle bir veritabanı varsa erişir, yoksa oluşturur.
im = vt.cursor() 

#yeni tablo oluşturalım
im.execute("CREATE TABLE IF NOT EXISTS kitaplar(ISBN INTEGER PRIMAY KEY, Kitap_Adi  , Yazar , Yayin_Tarihi , Tur, Ozet )")


def Kitap_Ekle():
    isbn=input("Isbn giriniz :")
    if  len(isbn)!=13:
        print ("ISBN no 13 karakterden oluşmalı")
        return(Kitap_Ekle())
    else:
        pass
    isim=input("Kitap adını giriniz : ")
    yazar=input("Yazarın adını giriniz : ")
    tarih=input("Yayın tarihini giriniz (dd.mm.yyyy): ")
    tur=input("Kitabın Türünü Giriniz : ")
    ozet=input("Özeti giriniz: ")
    
    liste=[(isbn,isim,yazar,tarih,tur,ozet)]
    komut='INSERT INTO kitaplar (ISBN, Kitap_Adi,Yazar,Yayin_Tarihi,Tur,Ozet) VALUES(?,?,?,?,?,?)'
    for kayit in liste:
        im.execute(komut,kayit)

    
def Kitap_Silme():
    silinecek_isbn=input("Silinecek kitabın isbn nosunu giriniz : ")
    sil_sonuc=im.execute(f"DELETE from kitaplar WHERE ISBN={silinecek_isbn}")
    if sil_sonuc.rowcount>0:
        print("Başarıyla Silindi.")
    else:
        print("Kitap bulunamadı.") 


def Kitap_Listeleme():
    im.execute('SELECT * FROM kitaplar')
    for veri in im:
        print(veri)
        
def Kitap_Ara():
    girilen_isbn=input("Aramak istediğiniz kitanın isbn no giriniz:")
    im.execute(f"SELECT * FROM kitaplar WHERE ISBN = {girilen_isbn}")
    print(im.fetchall())


        
#Menuyu yazdıralım: 
menu=UI(["Kitap Ekle","Kitap Ara","Kitap Sil","Kitap Listele","Çıkış"])
while True:
    menu.ShowMenu()
    choise=menu.GetChoise()
    if choise==1:Kitap_Ekle()
    elif  choise==2:Kitap_Ara()
    elif  choise==3:Kitap_Silme()
    elif choise==4:Kitap_Listeleme()
    else :break
vt.commit()
vt.close()