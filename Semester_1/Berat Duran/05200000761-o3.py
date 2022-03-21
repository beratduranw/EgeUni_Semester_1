hastaMaske = input("COVID-19 hastasında tıbbi maske takılmış olup olmadığını giriniz (e/h): ")
endikasyon = input("N95 endikasyonu olup olmadığını giriniz (e/h): ")
calisanMaske = input("Sağlık çalışanının maske kullanım durumunu giriniz (t: tıbbi, n: N95, h: hiçbiri):")
gozluk = input("Sağlık çalışanının göz koruyucu kullanıp kullanmadığını giriniz (e/h): ")
eldivenOnluk = input("Sağlık çalışanının eldiven&önlük kullanıp kullanmadığını giriniz (e/h):")

KKE = False
risk = ""

if endikasyon == "e" and calisanMaske == "n" and gozluk == "e" and eldivenOnluk == "e":
    KKE = True                                         # sağlık çalışanı uygun duruma göre ekipman kullandıysa KKE True
elif endikasyon == "h" and calisanMaske != "h" and gozluk == "e" and eldivenOnluk == "e":
    KKE = True

if KKE:
    print("Riskli değerlendirilmez")                            # KKE durumu
else:
    if hastaMaske == "e":                                       # hastada maske varsa ana if döngüsüne girer
        if calisanMaske == "h" or (endikasyon == "e" and calisanMaske == "t"):   # maskesi yoksa veya yetersizse durumu
            risk = "orta"
        elif gozluk == "h" and eldivenOnluk == "h":  # gözlük veya eldiven yosa düşük risk grubundadır
            risk = "düşük"
    else:                                                       # hastanın maskesi yok
        if calisanMaske == "h":
            risk = "yüksek"                                     # yüksek risk grubu olma şartı
        elif gozluk == "h" or (endikasyon == "e" and calisanMaske == "t"):    # orta risk grupları sadeleşmiş hali
            risk = "orta"
        elif eldivenOnluk == "h":                               # tek düşük risk durumu
            risk = "düşük"
    print("Sağlık çalışanı " + risk + " riskli kategoridedir.")

if risk == "yüksek":
    print("Semptom gelişmezse 7. günde PCR testi yapılması gereklidir.\nO güne kadar çalışamaz")
elif risk == "orta":
    print("Semptom gelişmezse 7. günde PCR testi yapılması gereklidir.\nO güne kadar çalışabilir.")
elif risk == "düşük":
    print("Semptom gelişmezse 7. günde PCR testi yapılması gerekli değildir.\nO güne kadar çalışabilir.")
