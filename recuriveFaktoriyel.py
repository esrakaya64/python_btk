while True:
    giris=int(input("Bir sayı giriniz:"))
    def faktoriyel(a):
        if a<0:
            print("Lütfen pozitif bir sayı giriniz")
        elif a<=1:
            return 1
        else:
            return a * faktoriyel(a-1)
    print(faktoriyel(giris))
    
        