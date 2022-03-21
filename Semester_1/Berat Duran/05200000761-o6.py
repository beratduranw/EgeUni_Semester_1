NEGATIFKONTROL = 0
SONAYNO = 12
IKIAYTOPLAM = 61


def hatali_veri():
    return input("Hatalı veri girdiniz, tekrar giriniz: ")


def ay_no_al():
    ay_no_scope = int(input("Ay numarasını giriniz: "))
    while NEGATIFKONTROL >= ay_no_scope or ay_no_scope > SONAYNO:
        ay_no_scope = int(hatali_veri())
    else:
        return ay_no_scope


def artik_yil_al():
    artik_yil_scope = input("Bu ayın ait olduğu yıl artık yıl mı: ")
    while artik_yil_scope not in ["e", "E", "h", "H"]:
        artik_yil_scope = hatali_veri()
    if artik_yil_scope == "e" or artik_yil_scope == "E":
        return True
    elif artik_yil_scope == "h" or artik_yil_scope == "H":
        return False


def gun_no_al(ay_no_scope, artik_yil_scope):
    aylar = 1
    toplam = 0
    ay_uzunlugu = 0
    while aylar <= ay_no_scope:  # toplama işlemi (son ay dahil olduğu için en son bu ayın değeri çıkartıldı)
        ay_uzunlugu = yilbasindan_itibaren_say(artik_yil_scope, aylar)      # gün no kontrolü için son ay
        toplam += ay_uzunlugu
        aylar += 1
    gun_no_scope = int(input("Gün numarasını giriniz: "))
    while NEGATIFKONTROL >= gun_no_scope or gun_no_scope > ay_uzunlugu:  # 0dan küçük ay uzunluğundan büyükse
        gun_no_scope = int(hatali_veri())
    toplam = toplam + gun_no_scope - ay_uzunlugu
    return toplam


def yilbasindan_itibaren_say(artik_yil_scope, aylar):           # her ay için gün sayısı ataması
    gun_sayi = 0
    if aylar in [1, 3, 5, 7, 8, 10, 12]:
        gun_sayi = 31
    elif aylar == 2:
        if artik_yil_scope:
            gun_sayi = 29
        else:
            gun_sayi = 28
    elif aylar in [4, 6, 9, 11]:
        gun_sayi = 30
    return gun_sayi


def tekrar_al():
    tekraralma = input("Devam etmek istiyoru musunuz: ")
    while tekraralma not in ["e", "E", "h", "H"]:
        tekraralma = hatali_veri()
    if tekraralma == "e" or tekraralma == "E":
        return True
    elif tekraralma == "h" or tekraralma == "H":
        return False


def main():
    tekrar = True
    while tekrar:
        ay_no = ay_no_al()
        artik_yil = artik_yil_al()
        gun_no = gun_no_al(ay_no, artik_yil)
        yilbasindan_itibaren_say(ay_no, gun_no)
        print("Yılbaşından bu tarihe kadar geçen gün sayısı: ", gun_no)
        tekrar = tekrar_al()


main()
