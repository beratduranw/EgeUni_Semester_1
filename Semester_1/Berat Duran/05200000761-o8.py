def hataliGirdi():
    try:
        veri = input("Uygun bir veri giriniz: ")
    except ValueError or TypeError or ZeroDivisionError:
        veri = hataliGirdi()
    return veri


def sinifAl():
    SINIFALTSINIR = 1
    SINIFUSTSINIR = 4
    try:
        sinif = int(input("Sınıfınızı giriniz: "))
        while not SINIFALTSINIR <= sinif <= SINIFUSTSINIR:
            sinif = int(hataliGirdi())
    except ValueError or TypeError:
        sinif = sinifAl()
    return sinif


def notOrtAl():
    try:
        ort = int(input("Lise not ortalamanızı giriniz: "))
        while not 0 <= ort <= 100:
            ort = int(hataliGirdi())
    except ValueError or TypeError:
        ort = notOrtAl()
    return ort


def liseAdiAl():
    # lise adının alınması
    try:
        liseAdi = input("Lisenizin adınız giriniz: ")
        while type(liseAdi[1]) is not str:
            liseAdi = hataliGirdi()
    except ValueError or TypeError or IndexError:
        liseAdi = liseAdiAl()
    return liseAdi.capitalize()


# puan dağılımı için
def sinifPuanDagilimiYap(sinifliste, notOrt, sinif):
    if (notOrt / 10) is int:
        sinifliste[sinif - 1][(notOrt // 10) - 1] += 1
    else:
        sinifliste[sinif - 1][notOrt // 10] += 1
    return sinifliste


def ilkTablo(liseAdOgrenciSay, liseAdOrtHesapla):
    # toplu input girişinde ilk çıktım gözükmüyor diye ekledim
    print("       Mezun Olunan Lise Adı                  Bölümdeki Öğrenci Sayısı        Not Ortalamaları")
    print("       Mezun Olunan Lise Adı                  Bölümdeki Öğrenci Sayısı        Not Ortalamaları")
    print("--------------------------------------        ------------------------        ----------------")
    for liseAd in liseAdOgrenciSay.items():
        print(liseAd[0], end=" " * (69 - len(liseAd[0])))
        print(liseAdOgrenciSay.get(liseAd[0]), end=" " * 19)
        print(format((liseAdOrtHesapla.get(liseAd[0])) / (liseAdOgrenciSay.get(liseAd[0])), ".2f"))


def ikinciTablo(sinifliste):
    toplamOgrenciSay = 0
    ARALIKSAYISI = 10
    SINIFSAYISI = 4
    print()
    print(" " * 53, "- Not Ortalaması -")
    print(
        "Sınıflar      0-10%    11-20%    21-30%    31-40%    41-50%    51-60%    61-70%    71-80%    81-90%   91-100%     Öğrenci say")
    print(
        "---------     -----    ------    ------    ------    ------    ------    ------    ------    ------   -------     -----------")
    # 4 satırlık tablo için döngü
    for sinif in range(SINIFSAYISI):
        sinifOgrenciSayisi = sum(sinifliste[sinif])
        toplamOgrenciSay += sinifOgrenciSayisi
        print(sinif + 1, ".Sınıf", end=" " * 5)
        for aralik in range(ARALIKSAYISI):
            try:
                x = str(format(sinifliste[sinif][aralik] * 100 / sinifOgrenciSayisi, ".2f")).rjust(6)
                print(x, end=" " * 4)
            except ZeroDivisionError:
                print("0", end=" " * 4)
        y = str(sinifOgrenciSayisi).rjust(12)
        print(y)
    print("Toplam bölüm", end="")
    # toplam bölüm satırı için döngü
    for aralik in range(ARALIKSAYISI):
        a = 0
        for sinif in range(SINIFSAYISI):
            a += 100 * sinifliste[sinif][aralik] / toplamOgrenciSay
        b = ("{:.2f}".format(a))
        b = b.rjust(7)
        print(b, end=" " * 3)
    print(" " * (12 - len(str(toplamOgrenciSay))), toplamOgrenciSay)


def main():
    devam = "e"

    DOGRULUK = ["E", "e"]
    TOPLAMDURUM = ["e", "E", "h", "H"]

    liseAdOgrenciSay = {}
    liseAdOrtHesapla = {}
    # iki boyutlu liste oluşturulması [[x] * 10] * 4 ile oluşturulmamıştır. Aynı adreslerde işlem yapılmaması için
    sinifliste = [[0] * 10, [0] * 10, [0] * 10, [0] * 10]
    while devam in DOGRULUK:

        # girdiler
        sinif = sinifAl()
        notOrt = notOrtAl()
        liseAd = liseAdiAl()
        # dict
        liseAdOgrenciSay[liseAd] = liseAdOgrenciSay.get(liseAd, 0) + 1
        liseAdOrtHesapla[liseAd] = liseAdOrtHesapla.get(liseAd, 0) + notOrt
        # boş listemiz sinif ve alınan puanlara göre listeye yerleştirilir
        sinifPuanDagilimiYap(sinifliste, notOrt, sinif)
        # süreklilik sorusu
        devam = input("Başka kullanıcı girmek istiyor musunuz: ")
        while devam not in TOPLAMDURUM:
            devam = input("Başka kullanıcı girmek istiyor musunuz: ")
    ilkTablo(liseAdOgrenciSay, liseAdOrtHesapla)
    ikinciTablo(sinifliste)


main()
