import math


class Kisi:
    def __init__(self, lNo, ad, elo, ukd, puan, bsNo, renk):
        self.lNo = lNo
        self.ad = ad
        self.elo = elo
        self.ukd = ukd
        self.puan = puan
        self.turlar = list()
        self.bsNo = bsNo
        self.renk = renk
        self.beles = False
        self.exRakip = list()
        self.eslesmis = False
        self.renkSay = 0
        self.bh1 = 0
        self.bh2 = 0
        self.sb = 0
        self.byeOlanaKadarkiPuan = 0
        self.gs = 0

    def getRenk(self):
        return self.renk

    def setEslesmis(self):
        self.eslesmis = True

    def setBeles(self):
        self.beles = True

    def setRenk(self, renk):
        self.renk = renk

    def setBsNo(self, bsNo):
        self.bsNo = bsNo

    def turEkle(self, rakip, renk, sonuc):
        tur = Tur(rakip, renk, sonuc)
        self.turlar.append(tur)

    def turlarPrintle(self):
        print(self.ad)
        for i in range(len(self.turlar)):
            self.turlar[i].turPrintle()

    def kisiyiPrintle(self):
        print(
            f"{self.bsNo:5}   {self.lNo:3}   {self.ad:23}    {self.elo:5}     {self.ukd:5}", end=" ")

    def digerRenk(self):
        return "sb".replace(self.renk, "")

    def eslesmisSifirla(self):
        self.eslesmis = False





class Tur:
    def __init__(self, rakip, renk, sonuc):
        self.rakip = rakip
        self.renk = renk
        self.sonuc = sonuc

    def getRakip(self):
        return self.rakip

    def turPrintle(self): 
        if type(self.rakip) == Kisi:
            print(
                f"rakibiniz: {self.rakip.bsNo}, kendi renginiz: {self.renk}, maç sonucu aldığınız puan: {self.sonuc} ")
        else:
            print("rakibiniz: '-', kendi renginiz: '-', maç sonucu aldığınız sonuc: 1")

    def getRenk(self):
        return self.renk


def veriAl():
    ad = input("Ad soyadınızı giriniz: ").replace("ç", "Ç").replace("i", "İ").replace("ö", "Ö").replace("ü",
                                                                                                        "Ü").upper()
    elo = int(input("Elonuzu giriniz: "))
    while elo < 1000 and elo != 0:
        elo = int(input("Hatalı elo!: "))
    ukd = int(input("Ukdnizi giriniz: "))
    while ukd < 1000 and ukd != 0:
        ukd = int(input("Hatalı ukd!: "))
    veri = [ad, elo, ukd]
    return veri


def kisileriOlustur():
    kisiler = list()
    lNoList = list()
    bsNo = 0
    while True:
        bsNo += 1
        lNo = int(input("Lisans numaranızı giriniz: "))
        while lNo in lNoList:
            lNo = int(
                input("Bu lisans numarası kullanılmıştır uygun bir değer giriniz:: "))
        if lNo <= 0:
            break
        else:
            lNoList.append(lNo)
            veri = veriAl()
            kisiler.append(Kisi(lNo, veri[0], veri[1], veri[2], 0, bsNo, "s"))

    return kisiler


def belesSort(kisiler):
    kisiler.sort(key=lambda x: x.beles, reverse=True)


def sortla(kisiler):
    abc = "ZYVÜUTŞSRPÖONMLKJİIHĞGFEDÇCBA "
    kisiler.sort(
        key=lambda x: (x.puan, x.elo, x.ukd, [abc.index(
            x.ad[a]) for a in range(len(x.ad))], 1 / x.lNo),
        reverse=True)


def sortlaBsnoAta(kisiler):
    sortla(kisiler)

    for i in range(len(kisiler)):
        kisiler[i].setBsNo(i + 1)


def kisileriYazdir(kisiler):
    print("\n BSNo   LNo   Ad-Soyad                     Elo       Ukd")
    print("-----   ---   -----------------------    -----     -----")
    for i in range(len(kisiler)):
        kisiler[i].kisiyiPrintle()
        print("")


def ikinciGirdiAl(kisiler):
    uzunluk = int(len(kisiler))
    tur = int(input("Tur sayısını giriniz: "))
    turMax = uzunluk - 1
    turMin = math.ceil(math.log2(uzunluk))
    renkler = ["b", "s", "B", "S"]
    while turMin > tur or tur > turMax:
        tur = int(input(f"Hatalı tur sayısı girdiniz: {turMin}-{turMax}: "))
    renk = input("İlk rengi giriniz: ").lower()
    while renk not in renkler:
        renk = input("Hatalı renk girdiniz: ").lower()
    digerRenk = "sb".replace(renk, "")
    return tur, renk, digerRenk


def eslesmisSifirla(kisiler):
    for i in kisiler:
        i.eslesmisSifirla()


def ilkRenkAta(kisiler, renk, digerRenk):
    for i in range(len(kisiler)):
        if i % 2 == 0:
            kisiler[i].setRenk(renk)
        if i % 2 == 1:
            kisiler[i].setRenk(digerRenk)


def turInputuAl():
    sonuc = int(input(f""))
    while sonuc not in [0, 1, 2, 3, 4, 5]:
        sonuc = int(input(f"masanın sonucunu yanlış girdiniz 1-5: "))
    return sonuc


def turRengiKontrolEt(kisi):
    if kisi.renkSay == 2:
        return False
    return True


def beyazBul(kisi, rakip):
    if kisi.renk == "b":
        return kisi
    elif rakip.renk == "b":
        return rakip
    else:
        return rakip


def macOlustur(kisiler):
    sortla(kisiler)
    eslesmisSifirla(kisiler)
    masa = []
    BYE = Kisi("-", None, None, None, None, "-", "-")
    if len(kisiler) % 2 == 1:
        for a in reversed(kisiler):
            if not a.beles:
                a.turEkle(BYE.lNo, BYE.renk, "1")
                a.setBeles()
                masa.append(a)
                a.setEslesmis()
                break
    for i in range(len(kisiler)):
        sortla(kisiler)
        if not kisiler[i].eslesmis:
            puanFarki = 0
            kisi = kisiler[i]
            uygunlar = uygunRakipleriBul(kisiler, kisi)
            while not rakipBul(kisi, uygunlar, masa, puanFarki):
                puanFarki += 0.5

    if len(kisiler) % 2 == 1:
        masa.append(masa[0])
        masa.pop(0)

    return masa


def sonucAl(kisiler, masa):
    if len(kisiler) % 2 == 1:
        dongu = len(masa) - 1
        masa[-1].puan += 1

    else:
        dongu = len(masa)

    for i in range(dongu):
        kisi = masa[i]
        rakip = kisi.exRakip[-1]
        sonuc = int(input(f"{i + 1}.masanın sonucunu giriniz: "))
        while sonuc not in [0, 1, 2, 3, 4, 5]:
            sonuc = int(input(f"{i + 1}.masanın sonucunu giriniz: "))
        if sonuc == 0:
            kisi.puan += 0.5
            rakip.puan += 0.5
            kisi.turlar[-1].sonuc = "½"
            rakip.turlar[-1].sonuc = "½"
        if sonuc == 1:
            kisi.puan += 1
            rakip.puan += 0
            kisi.turlar[-1].sonuc = "1"
            rakip.turlar[-1].sonuc = "0"
        elif sonuc == 2:
            kisi.puan += 0
            rakip.puan += 1
            kisi.turlar[-1].sonuc = "0"
            rakip.turlar[-1].sonuc = "1"
        elif sonuc == 3:
            kisi.puan += 1
            rakip.puan += 0
            kisi.turlar[-1].sonuc = "+"
            rakip.turlar[-1].sonuc = "-"
            kisi.setBeles()
        elif sonuc == 4:
            kisi.puan += 0
            rakip.puan += 1
            kisi.turlar[-1].sonuc = "-"
            rakip.turlar[-1].sonuc = "+"
            rakip.setBeles()
        elif sonuc == 5:
            kisi.puan += 0
            rakip.puan += 0
            kisi.turlar[-1].sonuc = "-"
            rakip.turlar[-1].sonuc = "-"


def rakipBul(kisi, uygunlar, masa, puanfarki):
    for rakip in uygunlar:
        if kisi.renk != rakip.renk and abs(kisi.puan - rakip.puan) <= puanfarki:
            birbir(kisi, rakip, masa)
        if kisi.eslesmis:
            return True
    if not kisi.eslesmis:
        for rakip in uygunlar:
            if kisi.renk == rakip.renk and turRengiKontrolEt(rakip) and abs(kisi.puan - rakip.puan) <= puanfarki:
                biriki(kisi, rakip, masa)
        if kisi.eslesmis:
            return True
    if not kisi.eslesmis:
        for rakip in uygunlar:
            if kisi.renk == rakip.renk and turRengiKontrolEt(kisi) and abs(kisi.puan - rakip.puan) <= puanfarki:
                biruc(kisi, rakip, masa)
        if kisi.eslesmis:
            return True
    return False


def uygunRakipleriBul(kisiler, kisi):
    uygunRakipler = []
    for rakip in kisiler:
        if rakip != kisi:
            if not (rakip in kisi.exRakip):
                if not kisi.eslesmis:
                    if not rakip.eslesmis:
                        uygunRakipler.append(rakip)
    return uygunRakipler


def biruc(kisi, rakip, masa):
    beyaz = beyazBul(kisi, rakip)
    masa.append(beyaz)

    kisi.setRenk(kisi.getRenk())
    rakip.setRenk(rakip.digerRenk())

    kisi.renkSay += 1
    rakip.renkSay = 1

    kisi.turEkle(rakip, kisi.digerRenk(), "0")
    rakip.turEkle(kisi, rakip.digerRenk(), "0")

    kisi.exRakip.append(rakip)
    rakip.exRakip.append(kisi)

    kisi.setEslesmis()
    rakip.setEslesmis()


def biriki(kisi, rakip, masa):
    beyaz = beyazBul(kisi, rakip)
    masa.append(beyaz)

    kisi.setRenk(kisi.digerRenk())
    rakip.setRenk(rakip.getRenk())

    kisi.renkSay = 1
    rakip.renkSay += 1

    kisi.turEkle(rakip, kisi.digerRenk(), "0")
    rakip.turEkle(kisi, rakip.digerRenk(), "0")

    kisi.exRakip.append(rakip)
    rakip.exRakip.append(kisi)

    kisi.setEslesmis()
    rakip.setEslesmis()


def birbir(kisi, rakip, masa):
    beyaz = beyazBul(kisi, rakip)
    masa.append(beyaz)

    kisi.setRenk(kisi.digerRenk())
    rakip.setRenk(rakip.digerRenk())

    kisi.renkSay = 1
    rakip.renkSay = 1

    kisi.turEkle(rakip, kisi.digerRenk(), "0")
    rakip.turEkle(kisi, rakip.digerRenk(), "0")

    kisi.exRakip.append(rakip)
    rakip.exRakip.append(kisi)

    kisi.setEslesmis()
    rakip.setEslesmis()


def masayiYazdir(kisiler, masa):
    if len(kisiler) % 2 == 1:
        for i in range(len(masa) - 1):
            print(
                f"{i+1:3} {masa[i].bsNo:4} {masa[i].lNo:5} {masa[i].puan:4.2f} - {masa[i].exRakip[-1].puan:4.2f} {masa[i].exRakip[-1].lNo:5} {masa[i].exRakip[-1].bsNo:4}")
        print(
            f"{len(masa):3} {masa[-1].bsNo:4} {masa[-1].lNo:5} {masa[-1].puan:4.2f} - BYE")
    else:
        for i in range(len(masa)):
            print(
                f"{i+1:3} {masa[i].bsNo:4} {masa[i].lNo:5} {masa[i].puan:4.2f} - {masa[i].exRakip[-1].puan:4.2f} {masa[i].exRakip[-1].lNo:5} {masa[i].exRakip[-1].bsNo:4}")


def main():
    kisiler = kisileriOlustur()
    sortlaBsnoAta(kisiler)
    kisileriYazdir(kisiler)
    print("")
    tur, ilkRenk, digerRenk = ikinciGirdiAl(kisiler)
    ilkRenkAta(kisiler, ilkRenk, digerRenk)
    print("")
    for turSayi in range(tur):
        masa = macOlustur(kisiler)
        print(f"{turSayi+1}. Tur Eşleştirme Listesi: ")
        print(f"        Beyazlar   Siyahlar        ")
        print(f"MNo BSNo   LNo Puan - Puan   LNo BSNo")
        print(f"--- ---- ----- ---- - ---- ----- ----")
        masayiYazdir(kisiler, masa)
        print("")
        sonucAl(kisiler, masa)
        print("")

    bhHesapla(kisiler, tur)
    sbgsHesapla(kisiler, tur)
    nihaiSortYazdir(kisiler)
    print("")
    caprazTabloYazdir(kisiler, tur)


def caprazTabloYazdir(kisiler, turSay):
    kisiler.sort(key=lambda x : x.bsNo)
    print("Çapraz Tablo: ")
    print("BSNo   SNo LNo   Ad-Soyad      Elo  UKD ", end="")
    for i in range(turSay):
        print(f"  {i+1}.Tur", end=" ")
    print("Puan  BH-1  BH-2    SB GS")
    print("------ --- ----- ------------ ---- ----", end=" ")
    for j in range(turSay):
        print("-"*7, end=" ")
    print("---- ----- ----- ----- --")
    for a in range(len(kisiler)):
        kisi = kisiler[a]
        print(f"{kisi.bsNo:6} {a+1:3} {kisi.lNo:5} {kisi.ad:<12} {kisi.elo:4} {kisi.ukd:4} ", end="")
        for tur in range(len(kisi.turlar)):
            turNo = kisi.turlar[tur]
            if kisi.turlar[tur].rakip != "-":
                print(f"  {turNo.rakip.bsNo} {turNo.renk} {turNo.sonuc} ",end="")
            else:
                print(f"  {turNo.rakip} {turNo.renk} {turNo.sonuc} ", end="")
        print(f"{kisi.puan:4.2f} {kisi.bh1:5.2f} {kisi.bh2:5.2f} {kisi.sb:5.2f} {kisi.gs:2}")



def nihaiSortYazdir(kisiler):
    print("Nihai Sıralama Listesi:")
    print("SNo BSNo   LNo Ad-Soyad      ELO  UKD Puan  BH-1  BH-2    SB GS")
    print("--- ---- ----- ------------ ---- ---- ---- ----- ----- ----- --")
    kisiler.sort(key = lambda x: (x.puan, x.bh1, x.bh2, x.sb), reverse=True) 
    i = 0
    for kisi in kisiler:
        i += 1
        print(f"{i:3} {kisi.bsNo:4} {kisi.lNo:5} {kisi.ad:12} {kisi.elo:4} {kisi.ukd:4} {kisi.puan:4.2f} {kisi.bh1:5.2f} {kisi.bh2:5.2f} {kisi.sb:5.2f} {kisi.gs:2}")
    


def bhHesapla(kisiler, turSay):
    for kisi in kisiler:
        rakipPuanListesi = list() 
        for tur in range(turSay):
            if kisi.turlar[tur].rakip != "-" and (kisi.turlar[tur].sonuc not in ["+", "-"]):
                rakipPuanListesi.append(kisi.turlar[tur].rakip.puan)

            else:
                byePuani = 0.5 * (turSay - tur - 1)
                for i in range(tur):
                    puan = kisi.turlar[i].sonuc
                    if puan == "1":
                        byePuani += 1
                    elif puan == "½":
                        byePuani += 0.5
                
                rakipPuanListesi.append(byePuani)
        rakipPuanListesi.sort(reverse=True)
        kisi.bh1 = sum(rakipPuanListesi[:-1])
        kisi.bh2 = sum(rakipPuanListesi[:-2])
    


def sbgsHesapla(kisiler, turSay):
    for kisi in kisiler:
        sbPuani = 0
        for tur in range(len(kisi.turlar)):
            if kisi.turlar[tur].sonuc == "1" and type(kisi.turlar[tur].rakip) == Kisi:
                sbPuani += kisi.turlar[tur].rakip.puan
                kisi.gs += 1

            elif kisi.turlar[tur].sonuc == "½":
                sbPuani += 0.5 * (kisi.turlar[tur].rakip.puan)
           
            elif kisi.turlar[tur].sonuc == "+" or kisi.turlar[tur].rakip == "-":
                if kisi.turlar[tur].sonuc == "+":
                    kisi.gs += 1
                sbPuani += 0.5 * (turSay - tur - 1)
                # o tura kadar toplam puan bulur            
                for i in range(tur):
                    puan = kisi.turlar[i].sonuc
                    if puan == "1":
                        sbPuani += 1
                    elif puan == "½":
                        sbPuani += 0.5

        kisi.sb = sbPuani

# 4. turda 88 numaralı kişiyi yanlış yerde yazdırıyor ama tur kaydında her şey doğru

main()
