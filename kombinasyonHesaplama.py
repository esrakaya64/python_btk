def faktoriyel(a):
    if a<0:
        print("Lütfen pozitif bir sayı giriniz")
    elif a<=1:
        return 1
    else:
        return a * faktoriyel(a-1)
    
print(faktoriyel(5))
    
def kombinasyon(b,c):
    if c>b:
        print("İkinci sayı birinci sayıdan küçük olmalı")
    elif  b<0 or c<0:
        print("Lütfen pozitif bir sayı giriniz")
    else:
        return faktoriyel(b)/(faktoriyel(c)+faktoriyel(b-c))
    
print(kombinasyon(4,2))