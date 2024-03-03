while True:
    try:#Hata olma olasılığı olan kod
        sayı1= int(input("Lütfen brinci sayıyı giriniz"))
        sayı2= int(input("Lütfen ikinci sayıyı giriniz"))
        sonuc=sayı1/sayı2
        print(f"işlemin sonucu {sonuc}")
    except ZeroDivisionError: #Belli bir hataya yönelik aldığımız önlem
        print("Bölen sayı sıfır olamaz")
    except ValueError as e : #Belli bir hataya yönelik verilecek uyarı sistemin mesajını versin
        print(e)
    except:#Öngöremediğimiz bir hataya yönelik aldığımız önlem
        print("Bir hata oluştu.")
    else:#Hata oluşmama durumunda yapılacak işlem
        print("İşlem başarılı")
    finally:#Hata oluşsa da oluşmasa da yapılacak işlem
        print("Program sonlandırıldı")
        
