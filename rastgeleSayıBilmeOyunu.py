
#! random modülünü içe aktar
import random

#! 1 ile 20 arasında rastgele bir tam sayı üret
sayı = random.randint(1, 20)

#! Kullanıcıdan kaç hakkı olacağını sor ve değeri al
can = int(input("Kaç hakkınız olsun: "))
#! Kullanıcının kalan haklarını takip eden değişken
hak = can
#! Tahmin sayısını takip eden sayaç
sayac = 0

#! Kullanıcının hakları bitene kadar döngüyü çalıştır
while hak > 0:
    #! Kullanıcının bir hakkını eksilt
    hak -= 1
    #! Tahmin sayacını bir artır
    sayac += 1
    #! Kullanıcıdan bir tahmin al
    tahmin = int(input("Tahmin yapın: "))
    
    #! Eğer tahmin doğruysa
    if sayı == tahmin:
        #! Kullanıcıyı tebrik et ve puanını hesapla, ardından oyunu sonlandır
        print(f"Tebrikler {sayac}. hakkınızda bildiniz. Toplam puanınız: {100 - (100/can) * (sayac-1):.2f}")
        break
    #! Eğer tahmin edilen sayı küçükse
    elif sayı > tahmin:
        #! Yukarı yönde olduğunu belirt
        print("Yukarı")
    #! Eğer tahmin edilen sayı büyükse
    else:
        #! Aşağı yönde olduğunu belirt
        print("Aşağı")
    
    #! Eğer haklar bitmişse
    if hak == 0:
        #! Kullanıcıya tutulan sayıyı ve puanını bildir
        print(f"Hakkınız bitti. Tutulan sayı {sayı}. Puanınız {100 - (100/can) * (sayac-1):.2f}")
