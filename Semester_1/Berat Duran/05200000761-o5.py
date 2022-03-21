kullaniciNo = 1
kullaniciAdet = 0      # kullanıcı girişini engelleyen değeri de saydığı için +1 den başlatıldı
urunAdet = 0           # ürün sayısı son çıkış değeri de sayıldığı için -1 alındı
satinAlinan = 0
finish = False
puanOrtalamasi = 0
iyipuan = 0
toplamIade = 0
iadeEden = 0
ikidenDusukOrtalama = 0
maxSatinAlan = 0
puanToplam = 0
puan = 0
besVerenler = 0
DORTBESVERENSAYISI = 3
MINPUAN = 1
MAXPUAN = 5
NEGATIFSAYIKONTROL = 0
IKIDENDUSUKORTALAMA = 2
# kullanıcı adet numara ve kontrol
maxSatinAlanStr = ""
puanOrt = 0
while not finish:
    # kullanıcı numrası kontrol -----------------------------------------------------------
    kullaniciNo = int(input("Kullanıcı numaranızı giriniz: "))
    if kullaniciNo > NEGATIFSAYIKONTROL:
        kullaniciAdet += 1
        # ürün adet ve kontrol-------------------------------------------------------------
        urunAdet = int(input("Aldığınız  ürün adedini giriniz: "))
        while urunAdet < NEGATIFSAYIKONTROL:
            urunAdet = int(input("Negatif ürün adedi girdiniz, aldığınız  ürün adedini giriniz: "))
        # iade kontrol---------------------------------------------------------------------
        iadeAdet = int(input("İade ettiğiniz ürün adedini giriniz: "))
        toplamIade += iadeAdet
        # iade adeti 0 dan küçük veya urun adetindne büyük olamaz--------------------------
        while iadeAdet < NEGATIFSAYIKONTROL or iadeAdet > urunAdet:
            iadeAdet = int(input("Geçersiz iade adedi girdiniz, iade ettiğiniz ürün adedini giriniz: "))
        if iadeAdet > 0:
            iadeEden += 1
        done = False
        puanToplam = 0
        iyipuan = 0
        while 0 <= iadeAdet < urunAdet and not done:

            satinAlinan = urunAdet - iadeAdet
            besVerenKullanici = False
            for i in range(satinAlinan):                      # satın alınan ürün kadar dönen döngü

                puan = int(input("Satın aldığınız ürüne puanınız: "))
                while puan < MINPUAN or puan > MAXPUAN:  # kontrol
                    puan = int(input("Tekrar aynı ürün için puan veriniz: "))

                if puan > DORTBESVERENSAYISI:        # 4 veya 5 puan verilen ürün sayısı
                    iyipuan += 1
                    if puan == 5:                        # eğer 5 puan verdiyse sayılmak üzere kullanıcı durumu kaydı
                        besVerenKullanici = True

                puanToplam += puan
            done = True
            if besVerenKullanici:                    # beş puan veren kullanıcı sayacı
                besVerenler += 1
        # her kullanıcı için print veri hesap ve atamaları ---------------------------------
        siparisAlmaOran = round(100 * satinAlinan / urunAdet, 2)
        puanOrtalamasi = round(puanToplam / satinAlinan, 2)
        dortVeyaBesPuanAlmis = round(100 * iyipuan / satinAlinan, 2)
        # her kullanıcının verilerini yazdırması için while içi print
        print(kullaniciNo, "Numaralı kullanıcının sipariş verdiği ürenleri alma oranı: %", siparisAlmaOran)
        print(kullaniciNo, "Numaralı kullanıcının satın aldığı ürünlere verdiği puan ortalaması: ", puanOrtalamasi)
        print(kullaniciNo, "Numaralı kullanıcının 4 veya 5 puan verdiği ürünlerin satın aldığı ürenler "   
                           "içindeki oranı: %", dortVeyaBesPuanAlmis)
        print("Bes veren kullanıcı ", besVerenler)
        int(maxSatinAlan)

        if maxSatinAlan < satinAlinan:
            maxSatinAlan = satinAlinan
            puanOrt = round(uanToplam / satinAlinan,2)
            maxSatinAlanStr = str(kullaniciNo)+"-"+str(satinAlinan)+"-"+str(iadeAdet)+"-"+str(puanOrt)
        if puanOrtalamasi < IKIDENDUSUKORTALAMA:
            ikidenDusukOrtalama += 1
    else:
        finish = True
# ----------------------------------------------------------------------------------------------------------------------
iadeKisiBasi = round(toplamIade / kullaniciAdet, 2)
iadeOran = round(100 * iadeEden / kullaniciAdet, 2)
zorBegenenSayi = kullaniciAdet - besVerenler
zorBegenenOran = round(100 * zorBegenenSayi / kullaniciAdet, 2)
ikidenDusukOran = round(100 * ikidenDusukOrtalama / kullaniciAdet, 2)

print("Kullanıcı başına iade edilen ürün sayısı: ", iadeKisiBasi)
print("Kullanıcılardan en az bir ürünü iade edenlerin tüm kullanıcılar içindeki oranı: %", iadeOran)
print("Satın aldığı hiçbir ürüne 5 puan vermeyen kullanıcı sayısı "
      "ve tüm kullanıcılar içindeki oranı: ", zorBegenenSayi, " %", zorBegenenOran)
print("Satın aldığı ürünlere verdiği puanların ortalaması 2’den düşük olan kullanıcı sayısı ve tüm"
      "kullanıcılar içindeki oranı:", ikidenDusukOrtalama, ",%", ikidenDusukOran)
print("En çok ürün satın alan kullanıcının numarası, satın aldığı ve iade ettiği ürün sayıları ile satın "
      "aldığı ürünlere verdiği puanların ortalaması: ", maxSatinAlanStr)
