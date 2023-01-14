import random
import time

print("""*****************
sayı tahmin etme oyunu
1 ile 40 arasında sayıyı tahmin edin.
*********************""")
rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7
while True:
    tahmin = int(input("Tahmininiz: "))

    if (tahmin < rastgele_sayı):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)

        print("daha yüksek bir sayı söyleyin...")

        tahmin_hakkı -= 1
    elif (tahmin > rastgele_sayı):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin....")
        tahmin_hakkı -= 1
    else:
        print("Bilgiler sorgulanıyor")
        time.sleep(1)
        print("tebrikler, sayınız: ",rastgele_sayı)
        break
    if (tahmin_hakkı == 0):
        print("tahmin hakkınız bitti...")
        print("sayımız: ", rastgele_sayı)