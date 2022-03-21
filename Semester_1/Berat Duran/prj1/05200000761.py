# constant
ASGARIUCRET = 2324.70
IKRAMIYE = ASGARIUCRET / 2
SATISKOMISYONU = 0.04
PRIMKOMISYONCEVIRI = 0.1
ENAZONADETKIRA = 10
ENAZYIRMIBESBINKIRA = 25000


def hataliGirdi():
    return input("Girdiğiniz değer hatalıdır, lütfen tekrar giriniz: ")


def bedelAl():  # gecici = bedel
    gecici = float(input("Satış / Kira bedelini giriniz: "))
    while gecici < 0:
        gecici = hataliGirdi()
    return gecici


# toplamKullanici = 0

maxKiraKonutBedeli = 0
maxKiraKonutAd = None

satilikKonutSayisi_son = 0
satilikIsyeriSayisi_son = 0
satilikArsaSayisi_son = 0

kiralikKonutSayisi_son = 0
kiralikIsyeriSayisi_son = 0
kiralikArsaSayisi_son = 0

satilikKonutBedeli_son = 0
satilikIsyeriBedeli_son = 0
satilikArsaBedeli_son = 0

maxSatilanSatisBedeli = 0
bedeliAsgaridenFazla = 0
satisYapmayanKullaniciSayisi = 0

maxSatilanEmlakTipi = None
maxSatilanDanismanAdi = None

maxSatisAdediAd = None
maxSatisAdediSay = 0
maxSatisAdediBedel = None

maxSatisBedeliAd = None
maxSatisBedeliSay = None
maxSatisBedeliBedel = 0

kotasiniDolduran = 0

primiMaasindanYuksek = 0

enAzDegeriSaglayanKullanici = 0

toplamUcret = 0

acenteKomisyonToplam = 0

maxPrimAlan = 0
minPrimAlanPrim = float('inf')

maxPrimAlanAd = None
maxPrimAlanMaas = 0
maxPrimAlanPrim = 0
maxPrimAlanAylik = 0

minPrimAlanAd = None
minPrimAlanMaas = 0
minPrimAlanAylik = 0

# her danışman için döngüye girer

danisman_sayisi = int(input("Danışman sayısını giriniz:"))
while danisman_sayisi < 0:
    baska_danisman = hataliGirdi()
for danisman_sayisi in range(danisman_sayisi):
    # toplam kullanıcı sayar
    # toplamKullanici += 1
    # başka bir kullanıcıya geçtiğinde sıfırlanması gereken değerler
    satilikKonutBedeli = 0
    satilikIsyeriBedeli = 0
    satilikArsaBedeli = 0
    kiralikKonutBedeli = 0
    kiralikIsyeriBedeli = 0
    kiralikArsaBedeli = 0
    satilikKonutSayisi = 0
    satilikIsyeriSayisi = 0
    satilikArsaSayisi = 0
    kiralikKonutSayisi = 0
    kiralikIsyeriSayisi = 0
    kiralikArsaSayisi = 0

    maxKiraKonutBedeli = 0
    maxKiraKonutAd = None

    # hata kontrollü input alımları
    ad = input("İsminizi giriniz: ")
    maas = float(input("Maaşınızı giriniz: "))
    while maas < ASGARIUCRET:
        maas = float(hataliGirdi())
    kota = float(input("Kotanızı giriniz: "))
    while kota < maas * 10:
        kota = float(hataliGirdi())
    emlakDongusu = True
    # her emlak için dönücek olan döngü
    while emlakDongusu:
        emlakTipi = input("Emlak tipini giriniz: ")  # emlak tipi alımı
        while emlakTipi not in ["k", "K", "i", "İ", "a", "A"]:
            emlakTipi = hataliGirdi()
        islemTuru = input("İşlem türünü giriniz: ")
        while islemTuru not in ["k", "K", "s", "S"]:  # işlem türü alımı
            islemTuru = hataliGirdi()
        # işlem türü ve emlak tipine göre ayırım ve depolamalar
        if islemTuru in ["s", "S"]:
            bedel = bedelAl()
            if emlakTipi in ["K", "k"]:
                satilikKonutBedeli += bedel
                satilikKonutSayisi += 1
            elif emlakTipi in ["İ", "i"]:
                satilikIsyeriBedeli += bedel
                satilikIsyeriSayisi += 1
            else:
                satilikArsaBedeli += bedel
                satilikArsaSayisi += 1
                # max satışın nitelikleri toplanır
            if maxSatilanSatisBedeli < bedel:
                maxSatilanEmlakTipi = emlakTipi
                maxSatilanSatisBedeli = bedel
                maxSatilanDanismanAdi = ad
        else:
            bedel = bedelAl()
            if emlakTipi in ["K", "k"]:
                kiralikKonutBedeli += bedel
                kiralikKonutSayisi += 1
                if maxKiraKonutBedeli < bedel:
                    maxKiraKonutBedeli = bedel
                    maxKiraKonutAd = ad
                if bedel > ASGARIUCRET:
                    bedeliAsgaridenFazla += 1
            elif emlakTipi in ["İ", "i"]:
                kiralikIsyeriBedeli += bedel
                kiralikIsyeriSayisi = 1
            else:
                kiralikArsaBedeli += bedel
                kiralikArsaSayisi += 1
        # başka emlak olup olmadığı kontrollü olarak sorulur
        emlakDongusu = input("Başka bir emlak tanımlamak istiyor musunuz?")
        while emlakDongusu not in ["e", "E", "h", "H"]:
            emlakDongusu = hataliGirdi()

        if emlakDongusu in ["e", "E"]:
            emlakDongusu = True
        else:
            emlakDongusu = False
            # döngü çıkışı ön hesaplar yapılır

            toplamSatisSayisi = satilikKonutSayisi + satilikIsyeriSayisi + satilikArsaSayisi
            toplamKiraSayisi = kiralikKonutSayisi + kiralikIsyeriSayisi + kiralikArsaSayisi
            toplamEmlakSayisi = toplamSatisSayisi + toplamKiraSayisi
            toplamKiraBedeli = kiralikKonutBedeli + kiralikIsyeriBedeli + kiralikArsaBedeli
            toplamSatisBedeli = satilikKonutBedeli + satilikIsyeriBedeli + satilikArsaBedeli
            satisKomisyonu = SATISKOMISYONU * toplamSatisBedeli
            kiraKomisyonu = toplamKiraBedeli
            toplamKomisyon = satisKomisyonu + kiraKomisyonu
            acenteKomisyonToplam += toplamKomisyon
            prim = toplamKomisyon * PRIMKOMISYONCEVIRI
            # hiç satış yapmayan kullanıcılar sayılır
            if toplamSatisSayisi == 0:
                satisYapmayanKullaniciSayisi += 1
            # max satış adedine sahip kullanıcı bilgileri
            if maxSatisAdediSay < toplamSatisSayisi:
                maxSatisAdediSay = toplamSatisSayisi
                maxSatisAdediAd = ad
                maxSatisAdediBedel = toplamSatisBedeli
            # max satış fiyatına sahip kullanıcı bilgileri
            if maxSatisBedeliBedel < toplamSatisBedeli:
                maxSatisBedeliAd = ad
                maxSatisBedeliSay = toplamSatisSayisi
                maxSatisBedeliBedel = toplamSatisBedeli
            # çıktılar
            print("Danışan adı:", ad)
            print("Bu ay sattığı emlak adedi: ", toplamSatisSayisi,
                  "oranı: %{:,.2f}".format(100 * toplamSatisSayisi / toplamEmlakSayisi))
            print("Bu ay kiralanan emlak adedi: ", toplamKiraSayisi,
                  "oranı: %{:,.2f}".format(100 * toplamKiraSayisi / toplamEmlakSayisi))
            print("Bu ay sattığınız konutların toplam bedeli: {:,.2f}TL".format(satilikKonutBedeli))
            print("Bu ay sattığınız iş yerlerinin toplam bedeli: {:,.2f}TL".format(satilikIsyeriBedeli))
            print("Bu ay sattığınız arsaların toplam bedeli: {:,.2f}TL".format(satilikArsaBedeli))
            print("Bu ay kiraladığınız konutların ortalama kira bedeli: {:,.2f}TL".format(
                kiralikKonutBedeli / kiralikKonutSayisi))
            print("Bu ay en yüksek bedel ile kiralanan konutun bedeli: {:,.2f}TL".format(maxKiraKonutBedeli))
            print("Maaşınız: {:,.2f}TL".format(maas))
            print("Priminiz: {:,.2f}TL".format(prim))
            if prim > maas:
                primiMaasindanYuksek += 1
            print("Kotanız: {:,.2f}TL".format(kota))
            print("Bu ay acentemize kazandırdığınız toplam konisyon: {:,.2f}TL".format(toplamKomisyon))
            # ücret hesabı ve ikramiye alınıp almayacağının belirlenmesi
            if toplamKomisyon < kota:
                print("Bu ay kotanızı doldurmadınız!")
                ucret = maas + prim
                print("Bu ay alacağınız toplam ücret: {:,.2f}TL".format(ucret))
            else:
                kotasiniDolduran += 1
                print("Bu ay kotanızı doldurdunuz!")
                ucret = maas + prim + IKRAMIYE
                print("Bu ay alacağınız toplam ücret: {:,.2f}TL".format(ucret))
            if toplamKiraSayisi >= ENAZONADETKIRA or (kiralikKonutBedeli + kiralikIsyeriBedeli + kiralikArsaBedeli) >= ENAZYIRMIBESBINKIRA:
                enAzDegeriSaglayanKullanici += 1
            # max prim alan kullanıcının belirenmesi
            if maxPrimAlan < prim:
                maxPrimAlan = prim
                maxPrimAlanAd = ad
                maxPrimAlanMaas = maas
                maxPrimAlanPrim = prim
                maxPrimAlanAylik = ucret
            # min prim alan kullanıcının belirenmesi
            if prim < minPrimAlanPrim:
                minPrimAlanAd = ad
                minPrimAlanMaas = maas
                minPrimAlanPrim = prim
                minPrimAlanAylik = ucret

            toplamUcret += ucret

            # başka emlak girdiğinde normalde sıfırlanan değerlerin sonrada yararlanmak için tutulması
            satilikKonutSayisi_son += satilikKonutSayisi
            satilikIsyeriSayisi_son += satilikIsyeriSayisi
            satilikArsaSayisi_son += satilikArsaSayisi
            kiralikKonutSayisi_son += kiralikKonutSayisi
            kiralikIsyeriSayisi_son += kiralikIsyeriSayisi
            kiralikArsaSayisi_son += kiralikArsaSayisi
            satilikKonutBedeli_son += satilikKonutBedeli
            satilikIsyeriBedeli_son += satilikIsyeriBedeli
            satilikArsaBedeli_son += satilikArsaBedeli

# bütün işlemler sorasındaki çıkışlar
toplamSatisSayisi_son = satilikKonutSayisi_son + satilikIsyeriSayisi_son + satilikArsaSayisi_son
toplamKiralikSayisi_son = kiralikKonutSayisi_son + kiralikIsyeriSayisi_son + kiralikArsaSayisi_son
print("\n")
print("Bu ay satılan konut sayısı: ", satilikKonutSayisi_son,
      "Oranı: %{:,.2f}".format(100 * satilikKonutSayisi_son / toplamSatisSayisi_son))
print("Bu ay satılan iş yeri sayısı: ", satilikIsyeriSayisi_son,
      "Oranı: %{:,.2f}".format(100 * satilikIsyeriSayisi_son / toplamSatisSayisi_son))
print("Bu ay satılan arsa sayısı: ", satilikArsaSayisi_son,
      "Oranı: %{:,.2f}".format(100 * satilikArsaSayisi_son / toplamSatisSayisi_son))
print("Bu ay kiralanan konut sayısı: ", kiralikKonutSayisi_son,
      "Oranı: %{:,.2f}".format(100 * kiralikKonutSayisi_son / toplamKiralikSayisi_son))
print("Bu ay kiralanan iş yeri sayısı: ", kiralikIsyeriSayisi_son,
      "Oranı: %{:,.2f}".format(100 * kiralikIsyeriSayisi_son / toplamKiralikSayisi_son))
print("Bu ay kiralanan arsa sayısı: ", kiralikArsaSayisi_son,
      "Oranı: %{:,.2f}".format(100 * kiralikArsaSayisi_son / toplamKiralikSayisi_son))
print("Bu ay satılan konutların bedeli: {:,.2f}TL".format(satilikKonutBedeli_son),
      "Ortalaması {:,.2f}TL".format(satilikKonutBedeli_son / satilikKonutSayisi_son))
print("Bu ay satılan iş yerlerinin bedeli: {:,.2f}TL".format(satilikIsyeriBedeli_son),
      "Ortalaması {:,.2f}TL".format(satilikIsyeriBedeli_son / satilikIsyeriSayisi_son))
print("Bu ay satılan arsaların bedeli:{:,.2f}TL".format(satilikArsaBedeli_son),
      "Ortalaması {:,.2f}TL".format(satilikArsaBedeli_son / satilikArsaSayisi_son))
print("Bu ay en yüksek bedelle satılan emlağın tipi: ", maxSatilanEmlakTipi,
      "satış bedeli: {:,.2f}TL".format(maxSatilanSatisBedeli), "satış yapan danışmanın adı: ", maxSatilanDanismanAdi)
print("Bu ay en yüksek bedelle kiralanan konutun kira bedeli: {:,.2f}TL".format(maxKiraKonutBedeli),
      "Kiralayan danışmanın adı: ", maxKiraKonutAd)
print("Bu ay kiralanan konutlardan kira bedeli Asgari ücretten fazla olan konutların sayısı: ", bedeliAsgaridenFazla,
      "kiralanan konutlar içindeki oranı: %{:,.2f}".format(100 * bedeliAsgaridenFazla / kiralikKonutSayisi_son))
print("Bu ay hiç satış yapmayan danışmanların sayısı: ", satisYapmayanKullaniciSayisi,
      "tüm danışmanlar içindeki oranı: %{:,.2f}".format(100 * satisYapmayanKullaniciSayisi / danisman_sayisi))
print("Bu ay en çok sayıda satış yapan kullanıcının adı: ", maxSatisAdediAd, "sattığı emlak sayısı: ", maxSatisAdediSay,
      "sattığı emlakların toplam bedeli: {:,.2f}TL".format(maxSatisAdediBedel))
print("Bu ay en çok kazanç sağlayan kullanıcının adı: ", maxSatisBedeliAd, "sattığı emlak sayısı: ", maxSatisBedeliSay,
      "sattığı emlakların toplam bedeli: {:,.2f}TL".format(maxSatisBedeliBedel))
print("Bu ay kotasını dolduran kullanıcı sayısı: ", kotasiniDolduran,
      "tüm danışmanlar içindeki oranı: %{:,.2f}".format(100 * kotasiniDolduran / danisman_sayisi))
print("Bu ay primi maaşından yüksek olan kullanıcı sayısı: ", primiMaasindanYuksek,
      "tüm danışmanlar içindeki oranı: %{:,.2f}".format(100 * primiMaasindanYuksek / danisman_sayisi))
print("Bu ay en az 10 adet veya en az 25.000 TL turarında emlak kiralayan kullanıcı sayısı: ",
      enAzDegeriSaglayanKullanici)
print("Bu ay en yüksek prim alan kullanıcı: ", maxPrimAlanAd, "maaşı: {:,.2f}TL".format(maxPrimAlanMaas),
      "primi: {:,.2f}TL".format(maxPrimAlanPrim), "bu ay alacağı ücreti: {:,.2f}TL".format(maxPrimAlanAylik))
print("Bu ay en az prim alan kullanıcı: ", minPrimAlanAd, "maaşı: {:,.2f}TL".format(minPrimAlanMaas),
      "primi: {:,.2f}TL".format(minPrimAlanPrim), "bu ay alacağı ücreti: {:,.2f}TL".format(minPrimAlanAylik))
print("Bu ay danışanlara ödenecek olan toplam ücret: {:,.2f}TL".format(toplamUcret),
      "ortalaması: {:,.2f}TL".format(toplamUcret / danisman_sayisi))
print("Bu ay acentemizin kazandığı toplam komisyon: {:,.2f}TL".format(acenteKomisyonToplam))
