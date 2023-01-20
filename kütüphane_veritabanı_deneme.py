from kütüphane import *
print("""
***********************
KÜTÜPHANE PROGRAMINA 
HOŞ GELDİNİZ...

İŞLEMLER

1. KİTAPLARI GÖSTER

2. KİTAP SORGULAMA

3. KİTAP EKLE

4. KİTAP SİL

5. BASKI YÜKSELT

6. ÇIKMAK İÇİN q'YE BASINIZ....
**********************
""")
kütüphane = Kütüphane()
while True:
    işlem = input("YAPACAĞINIZ İŞLEM:")
    if işlem == "q":
        print("PROGRAM SONLANDIRILIYOR....")
        print("YİNE BEKLERİZ....")
        break
    elif (işlem == "1"):
        kütüphane.kitapları_göster()
    elif(işlem == "2"):
        isim = input("HANGİ KİTABI İSTİYORSUNUZ?")
        print("KİTAP SORGULANIYOR...")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
    elif (işlem=="3"):
        isim = input("İSİM:")
        yazar = input("YAZAR:")
        yayınevi = input("YAYINEVİ:")
        tür = input("TÜR:")
        baskı = input("BASKI:")
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("KİTAP EKLENİYOR...")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("KİTAP EKLENDİ...")
    elif(işlem=="4"):
        isim = input("HANGİ KİTABI SİLMEK İSTİYORSUNUZ?")
        cevap = input("EMİN MİSİNİZ?(E/H)")
        if cevap == "E":
            print("KİTAP SİLİNİYOR...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("KİTAP SİLİNDİ...")
    elif(işlem=="5"):
        isim = input("HANGİ KİTABIN BASKISINI YÜKSELTMEK İSTİYORSUNUZ?")
        print("BASKI YÜKSELKTİLİYOR")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("BASKI YÜKSELTİLDİ...")
    else:
        print("GEÇERSİZ İŞLEM...")
