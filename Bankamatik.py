
                                         #!BANKAMATİK UYGULAMASI

#  Kullanıcı 2'ye ait hesap bilgilerini içeren sözlük
hesapYuksel = {
    "ad": "Kullanıcı2",  # Hesap sahibinin adı
    "hesapNo": "123456",  # Hesap numarası
    "bakiye": 4000,  # Hesaptaki mevcut bakiye
    "ekHesap": 1500  # Ek hesap limiti
}

# Kullanıcı 1'e ait hesap bilgilerini içeren sözlük
hesapMuco = {
    "ad": " Kullanıcı1",  # Hesap sahibinin adı
    "hesapNo": "654321",  # Hesap numarası
    "bakiye": 2000,  # Hesaptaki mevcut bakiye
    "ekHesap": 500  # Ek hesap limiti
}

# Hesapları içeren bir sözlük
hesaplar = {
    "1": hesapYuksel,  # İlk hesap Yüksel YENİYIL'a ait
    "2": hesapMuco  # İkinci hesap Mücahit Yeniyıl'a ait
}

# Hesap seçme fonksiyonu
def hesapSec():
    # Kullanıcıya hangi hesap ile işlem yapmak istediğini soruyoruz
    print("Hangi hesap ile işlem yapmak istiyorsunuz?")
    print("1. Kullanıcı 2")
    print("2. Kullanıcı 1")
    secim = input("Seçiminiz (1/2): ")  # Kullanıcının seçimini alıyoruz
    return hesaplar.get(secim)  # Seçilen hesabı döndürüyoruz

# Para çekme işlemi için fonksiyon tanımlama
def ParaCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")  # Hesap sahibine selam veriyoruz
    
    # Hesap bakiyesi yeterliyse doğrudan para çekiliyor
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar  # Bakiye miktar kadar düşülüyor
        print("Paranızı alabilirsiniz")
    else:
        # Toplam bakiye (normal bakiye + ek hesap) kontrol ediliyor
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        
        # Toplam bakiye yeterliyse ek hesap kullanımı soruluyor
        if toplam >= miktar:
            ekHesapKullanimi = input("Ek hesap kullanılsın mı? (e/h)")
            
            # Kullanıcı ek hesap kullanmayı onaylarsa
            if ekHesapKullanimi == "e":
                ekHesapKullanılacakMiktar = miktar - hesap["bakiye"]  # Ek hesap kullanılacak miktar hesaplanıyor
                hesap["bakiye"] = 0  # Hesap bakiyesi sıfırlanıyor
                hesap["ekHesap"] -= ekHesapKullanılacakMiktar  # Ek hesaptan düşülüyor
                print("Paranızı alabilirsiniz")
            else:
                # Ek hesap kullanılmazsa mevcut bakiye bilgisi gösteriliyor
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır")
        else:
            # Toplam bakiye de yeterli değilse para çekilemeyeceği belirtiliyor
            print("Üzgünüz, bakiyeniz yetersiz")

# Para yatırma işlemi için fonksiyon tanımlama
def ParaYatir(hesap, miktar):
    hesap["bakiye"] += miktar  # Yatırılan miktar bakiyeye ekleniyor
    print(f"{miktar} TL hesabınıza yatırıldı. Güncel bakiyeniz: {hesap['bakiye']} TL")

# Bakiyeyi sorgulama fonksiyonu
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

# Hesap seçme
secilenHesap = hesapSec()  # Kullanıcıdan hangi hesabı kullanmak istediğini öğreniyoruz

if secilenHesap:  # Geçerli bir hesap seçildiyse
    işlem = input("Ne işlem yapmak istiyorsunuz? (Yatırma/Çekme)")  # Kullanıcıdan işlem türünü alıyoruz

    if işlem == "Çekme":  # Kullanıcı çekme işlemi yapmak istiyorsa
        ÇekilecekTutar = int(input("Ne kadar çekmek istiyorsunuz?"))  # Çekilecek tutarı alıyoruz
        ParaCek(secilenHesap, ÇekilecekTutar)  # Para çekme fonksiyonunu çağırıyoruz
    elif işlem == "Yatırma":  # Kullanıcı yatırma işlemi yapmak istiyorsa
        YatirilacakTutar = int(input("Ne kadar yatırmak istiyorsunuz?"))  # Yatırılacak tutarı alıyoruz
        ParaYatir(secilenHesap, YatirilacakTutar)  # Para yatırma fonksiyonunu çağırıyoruz
    else:
        print("Geçersiz işlem türü. Lütfen 'Yatırma' veya 'Çekme' yazınız.")

    bakiyeSorgula(secilenHesap)  # İşlemden sonra bakiyeyi sorguluyoruz
else:
    print("Geçersiz hesap seçimi.")  # Geçersiz hesap seçimi yapıldıysa kullanıcıyı bilgilendiriyoruz
