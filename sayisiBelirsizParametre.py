#Tek yıldız kullanırsak methoda gönderilen argümanları tupple olarak alır:
def Topla(*sayilar):
    print (type(sayilar)) #Tuple olduğunu buradan görebilirsiniz.
    toplam =0
    for sayi in sayilar:
        toplam += sayi
    return toplam
    

print(Topla(2,3,5,6))
print(Topla(4,5))
print(Topla(56,56))


#Çift yıldız kullanırsak methoda gönderilen argümanları dictionary olarak alır
def toplama(**sayilarimiz):
    toplam = 0
    print (type(sayilarimiz)) #Dictionary olduğunu buradan görebilirsiniz.
    for key, value in sayilarimiz.items():
        toplam += value
    return toplam


print(toplama(a=5, b=3)) 
print(toplama(x=10, y=20, z=30))  
