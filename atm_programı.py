print(""""*****************************************
Atm Makinesine Hoş geldiniz...
işlemler:
1. bakiye sorgulama

2. para yatırma

3. para çekme

programdan çıkmak için q'yw basın
***********************************************""")

bakiye = 1000
while True:
    işlem = input("İşlemi seçiniz: ")

    if (işlem == "q"):
        print("yine bekleriz...")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Miktarı giriniz: "))
        bakiye += miktar
    elif (işlem == "3"):
        miktar = int(input("Miktarı giriniz: "))

        if (bakiye - miktar < 0):
            print("Böyle bir miktar çekemezsiniz...")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz İşlem....")