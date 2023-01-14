import random
import time

class Kumanda():

    def __init__(self,tv_durum = "kapalı", tv_ses = 0, kanal_listesi = ["trt", "kanal d"], kanal = "trt"):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

    def tv_ac(self):

        if (self.tv_durum == "açık"):
            print("televizyon zaten açık....")
        else:
            print("televizyon açılıyor....")
            self.tv_durum = "açık"
    def tv_kapat(self):
        if (self.tv_durum == "kapalı"):
            print("televizyon zaten kapalı....")
        else:
            print("televizyon kapanıyor.....")
            self.tv_durum = "kapalı"
    def ses_ayarları(self):
        while True:

            cevap = input("sesi azalt: < \n sesi yükselt: > \n çıkış : çıkış")

            if cevap == "<":
             if self.tv_ses != 0:

                self.tv_ses -= 1
                print("ses", self.tv_ses)
            elif (cevap == ">"):
                if self.tv_ses != 31:
                    self.tv_ses += 1

                    print("ses: ", self.tv_ses)

            else:
                print("ses güncellendi", self.tv_ses)
                break

    def kanal_ekle(self, kanal_ismi):
        print("kanal eklenşyor....")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("kanal eklendi.....")
    def rastgele_kanal(self):

        rastgele = random.randint(0, len(self.kanal_listesi) - 1)

        self.kanal = self.kanal_listesi[rastgele]

        print("şu anki kanal: ", self.kanal)
    def __len__(self):

        return len(self.kanal_listesi)
    def __str__(self):

        return "Tv durumu: {}\nTv ses: {}\nKanal listesi: {}\n Şu anki kanal: {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)
kumanda = Kumanda()
print("""
    
    TELEVİZYON UYGULAMASI
    
    1. TV AÇ
    
    2. TV KAPAT
    
    3. SES AYARLARI
    
    4. KANAL EKLE
    
    5. KANAL SAYISINI ÖĞRENME
    
    6. RASTGELE KANALA GEÇME
    
    7. TELEVİZYON BİLGİLERİ
    
    ÇIKMAK İÇİN Q'YE BASIN """)
while True:
    işlem = input("İŞLEMİ SEÇİNİZ: ")
    if işlem == "q":
        print("PROGRAM SONLANDIRILIYOR....")
        break
    elif (işlem == "1"):
        kumanda.tv_ac()
    elif işlem == "2":
        kumanda.tv_kapat()
    elif işlem == "3":
        kumanda.ses_ayarları()
    elif işlem == "4":
        kanal_isimleri = input("kanal isimlerini ',' ile ayırarak giriniz:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif işlem == "5":
        print("kanal sayısı: ", len(kumanda))

    elif işlem == "6":
        kumanda.rastgele_kanal()
    elif işlem == "7":
        print(kumanda)
    else:
        print("geçersiz işlem.....")

