def main():
    try:

        f = open("secim.txt", "r")
        parti_sayisi = int(f.readline())
        il_sayisi = int((len(f.readlines()))/(parti_sayisi + 2))
        # parti sayısı ve il sayısı değişkenlerinden sonra gerekli kısımdan oknmaya devam edilmesi
        f.seek(3)  # [0,1,2] = [8,\,n] ==> [3] = parti sayısı sonrasındaki ilk değer değer

        trtoplam_kontenjan = 0
        trtoplam_oy = 0
        # parti sayısı genişliğinde liste oluşturulması
        tr_oy_say = [0] * parti_sayisi
        tr_mv_say = [0] * parti_sayisi
        sifir_mv_il_say = [0] * parti_sayisi

        for i in range(il_sayisi):
            lst = lst_olusturma(parti_sayisi, f)
            mv_lst = mv_lst_sifirlama(parti_sayisi)
            mvlst, initiallst = tablo_olustur_mv_list_dondur(lst, mv_lst, parti_sayisi)

            for j in range(parti_sayisi):
                tr_oy_say[j] += initiallst[j]
                tr_mv_say[j] += mvlst[j]
                if mvlst[j] == 0:
                    sifir_mv_il_say[j] += 1
            # print(tr_oy_say)  # genel oy sayısı bulma doğru

            print("\n")
            trtoplam_kontenjan += toplam_mv_bul(mvlst)
            trtoplam_oy += toplam_oy_bul(initiallst)
        # son çıktılar
        print("Turkiye Geneli")
        print("Milletvekili Kontenjanı: ", trtoplam_kontenjan)
        print("Geçerli oy sayısı: ", trtoplam_oy)
        print("")
        f.close()
        tr_tablo_yap(parti_sayisi, tr_oy_say, trtoplam_oy, tr_mv_say, trtoplam_kontenjan, sifir_mv_il_say)
    except FileNotFoundError:
        print("Bu dosya bulunamadı")


def tr_tablo_yap(parti_say, tr_oy_say, trtoplam_oy, tr_mv_say, trtoplam_kontenjan, sifir_mv_il_say):
    # tr geneli tablosunun oluşturulması
    print("Pusula Sıra   Oy Sayısı   Oy Yuzde   MV Say   MV Yuzde   0 MV Il Say")
    print("-----------   ---------   --------   ------   --------   -----------")
    for i in range(parti_say):
        print(format(i + 1, "11d"), end="   ")  # parti no

        # türkiye geneli oy sayısı kontrol ve çıktısı
        print(format(tr_oy_say[i], "9d"), end="   ")
        try:
            print(format(tr_oy_say[i] / trtoplam_oy * 100, "7.2f"), end="%  ")
        except ZeroDivisionError:
            print(format(0.00, "15.2f"))

        # türkiye geneli mv sayısı kontrol ve çıktısı
        print(format(tr_mv_say[i], "6d"), end="   ")
        try:
            print(format(tr_mv_say[i] / trtoplam_kontenjan * 100, "8.2f"), end="%  ")
        except ZeroDivisionError:
            print(format(0.00, "15.2f"))
        print(format(sifir_mv_il_say[i], "12d"))


def tablo_olustur_mv_list_dondur(lst, mv_lst, parti_sayisi):
    # her il için tablo ve sonradan kullanılması için son mv listesi returnu
    # fonksiyon içerisindeki plaka kodu ve mv kontenjan sayısının çıkarılması
    plaka_kodu = lst[0]
    lst.pop(0)
    mvsayisi = lst[0]
    lst.pop(0)

    toplam_oy_sayisi = 0
    print("İl plaka kodu: ", plaka_kodu)
    print("Milletvekili kontenjanı: ", mvsayisi)

    for j in range(parti_sayisi):  # geçerli oy sayısı için döngü ile toplama işlemi
        toplam_oy_sayisi += lst[j]
    print("Geçerli oy sayısı: ", toplam_oy_sayisi)
    print("Pusula Sira   Oy Say   Oy yüzde   Millet Vekili Sayısı")
    print("-----------   ------   --------   --------------------")
    # max bulurken tam bölmeden önceki değerlerin bulunduğu liste
    initiallst = lst[:]

    for mv_sayisi_bul in range(mvsayisi):
        max_oy_alan_parti = max(lst)
        lstindex = lst.index(max_oy_alan_parti)
        lst[lstindex] = max_oy_alan_parti // 2
        mv_lst[lstindex] += 1

    for parti_say in range(parti_sayisi):  # her parti için tablo çıktısı
        print(format(parti_say + 1, "11d"), end="   ")  # parti no
        print(format(initiallst[parti_say], "6d"), end="   ")  # parti oy sayisi
        # parti oy yüzdesi
        try:
            print(format(initiallst[parti_say] / toplam_oy_sayisi * 100, "7.2f"), end="%  ")
        except ZeroDivisionError:
            print(format(0.00, "15.2f"))

        # parti kantenjan
        print(format(mv_lst[parti_say], "21d"))
    return mv_lst, initiallst


def toplam_oy_bul(initiallst):  # türkiye geneli için toplam oy
    toplam = 0
    length = len(initiallst)
    for i in range(length):
        toplam += initiallst[i]
    return toplam


def toplam_mv_bul(mvlst):   # türkiye geneli için mv toplam
    toplam = 0
    length = len(mvlst)
    for i in range(length):
        toplam += mvlst[i]
    return toplam


def il_plaka_kodu_al(x):
    il_plaka_kodu = int(x.readline())
    return il_plaka_kodu


def milletvekili_kontenjan_al(x):
    milletvekili_kontenjan = int(x.readline())
    return milletvekili_kontenjan


def parti_oy_sayisi_al(x):
    parti_oy_sayisi = int(x.readline())
    return parti_oy_sayisi


def lst_olusturma(parti_sayisi, x):
    lst = [il_plaka_kodu_al(x), milletvekili_kontenjan_al(x)]
    for parti_say in range(parti_sayisi):
        lst.append(parti_oy_sayisi_al(x))
    return lst


def mv_lst_sifirlama(parti_sayisi):     # mv listesini her il için sıfırlama
    mv_lst = [0] * parti_sayisi
    return mv_lst


main()
