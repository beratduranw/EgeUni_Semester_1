# COVİD-19 hastalığı ile ilgili hastalık belirtisi vermeyen olgular olabileceği bildirmekle birlikte bunların
# oranının kaç olduğu kesin olarak bilinmemektedir. Şimdiye kadar elde edilen verilere göre, hastalığın yaklaşık %15
# hastada ağır seyrettiği, yaklaşık %2 hastada da ölümle sonuçlandığı bilinmektedir. Ayrıca bir testin maliyetinin
# 125 TL, hastalığı hafif seyreden bir hastanın tedavı masrafının yaklaşık 1.250 TL, ağır seyreden bir hastann tedavi
# masrafının yaklaşık 12.500 TL olduğu bilinmektedir.
# Bir şehirde yaşayan tüm insanlara COVId-19 testi yapılarak hiçbir olgu kalmayıncaya kadar tam karantina ve izolasyon
# uygulanmasına karar verilmiştir. Buna göre, şehirde yaşayan insan sayısını, testler sonucunda saptanan olgu sayısını
# ve hasta sayısını kullanıcıdan alan ve aşağıda listelenen çıktıları ekrena yazdıran bir program yazdırınız:

nufus = int(input("Şehirde yaşayan insan sayısını giriniz: "))
olgu = int(input("Testler sonucunda saptanan olgu sayısını giriniz: "))
hasta = int(input("Hasta sayısını giriniz: "))
# nufus = int(12345)    denemeler sırasında oto input için kullanılmıştır
# olgu = int(1234)
# hasta = int(234)
hafif = round(hasta * 0.85)
agir = round(hasta * 0.15)
olu = round(hasta * 0.02)
test_maliyeti = nufus*125
hafif_hasta_maliyeti = hafif * 1250
agir_hasta_maliyeti = agir * 12500
nhasta_bolu_olgu = float(100*(olgu - hasta) / olgu)
toplam_maliyet = (test_maliyeti+hafif_hasta_maliyeti+agir_hasta_maliyeti)
ort = toplam_maliyet/nufus
print("Olgu sayısının nüfusa oranı: %{:,.3f}".format(olgu / nufus * 100))
print("Hastalık belirtisi vermeyen olgu sayısı: ", int(olgu - hasta))
print("Hastalık belirtisi vermeyen olguların tüm olgular içindeki oranı: %{:,.3f}".format(nhasta_bolu_olgu))
print("Süreç boyunca karşılaşılacak yaklaşık ağır hasta: ", agir)
print("Süreç boyunca karşılaşılacak yaklaşık ölüm sayısı: ", olu)
print("Hastalığın şehir bütçesine getireceği yaklaşık toplam maliyet: {:,.2f} TL".format(toplam_maliyet))
print("Hastalığın tüm nüfus dikkate alındığında yaklaşık kişi başır ortalama maliyeti: {:,.2f} TL".format(ort))
