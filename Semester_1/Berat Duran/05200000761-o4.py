soruDevamliligi = "e"
iosSayaci = 0
androidSayaci = 0
memnunDegil = 0
ortaMemnun = 0
iyi = 0
yil = 12
yilSay = 0
yilDegerlendirme = 0
yilMemnun = 0
kullanicisay = 0
iosMemnuniyetToplam = 0
androidMemnuniyetToplam = 0
memnunDegilSure = 0
silenSayac = 0
memnuniyetToplam = 0

while soruDevamliligi == "e":
    soruDevamliligi = input("Kullanıcı girişi için 'e'ye basınız: ")

    if soruDevamliligi == "e":
        kullanicisay += 1
        sistem = input("Cihazınızın işletim sistemi nedir: ")
        sure = int(input("Uygulamayı kaç ay boyunca kullandınız: "))  # kullanıcının uygulamayı kullandığı süre
        memnun = int(input("Uygulamamızdan ne derece memnun kaldınız: "))  # kullanıcının memnuniyet düzeyi
        # sistem ayırma bloğu
        if sistem == 'i':
            iosSayaci += 1                          # ios kullanıcı sayısı
            iosMemnuniyetToplam += memnun
        elif sistem == 'a':
            androidSayaci += 1                      # android kullanıcı saysısı
            androidMemnuniyetToplam += memnun
        # memniniyet bloğu
        if memnun == 1:
            memnunDegil += 1                        # memnun olmayan kullanici sayısı sayacı
            memnunDegilSure += sure                 # memnun olmayan kullaniciların toplam kullanma süresi
        elif memnun == 2:
            ortaMemnun += 1                         # eh memnun kullanici sayısı sayacı
        elif memnun == 3:
            iyi += 1                                # memnun kullanici sayısı
        # en az bir yıl kullananların değerlendirme bloğu
        if sure > yil:                              # bir yıl üstünde kullananların görüş değerlendirmesi
            yilDegerlendirme += sure                # yıldan fazla kullananların sure toplamı İLERDE BOLUP ORT BUL
            yilSay += 1                             # yıldan fazla kullanan sayısı sayacı
            yilMemnun += memnun                     # yıldan fazla kullananların memnuniyeti İLERDE BÖLÜP ORT BUL
        # 1 aydan önce silenlerin sayımı
        elif sure < 1:
            silenSayac += 1
    # kategorilendirme sonu print fonksiyon başlangıcı
    elif soruDevamliligi == "h":
        # sonrada kullanılabilmesi için her değer bir değişkene atanmıştır
        memnuniyetToplam = iosMemnuniyetToplam + androidMemnuniyetToplam
        memnunKullaniciYuzdesi = 100 * iyi / kullanicisay
        print("\nUygulamadan memnun kullanıcıların sayısı: {}, Yüzdesi: %{:,.2f}"
              .format(iyi, memnunKullaniciYuzdesi))
        # ne memnun ne değil kullanıcı bloğu
        ehMemnunYuzdesi = 100 * ortaMemnun / kullanicisay
        print("Uygulamadan ne memnun ne memnun değil olan kullanıcıların sayısı: {}, Yüzdesi: %{:,.2f}"
              .format(ortaMemnun, ehMemnunYuzdesi))
        # memnun olmayanların bloğu
        memnunDegilYuzdesi = 100 * memnunDegil / kullanicisay
        print("Uygulamadan memnun olmayan kullanıcıların sayısı: {}, Yüzdesi: %{:,.2f}"
              .format(memnunDegil, memnunDegilYuzdesi))
        # ios bloğu
        iosKullaniciOrani = 100 * iosSayaci / kullanicisay
        iosMemnuniyetOrtalamasi = iosMemnuniyetToplam / iosSayaci
        print("IOS kullanıcılarının oranı: %{:,.2f}, Memnuniyet ortalaması: {:,.2f}"
              .format(iosKullaniciOrani, iosMemnuniyetOrtalamasi))
        # android bloğu
        androidKullaniciOrani = 100 * androidSayaci / kullanicisay
        androidMemnuniyetOrtalamasi = androidMemnuniyetToplam / androidSayaci
        print("Android kullanıcılarının oranı: %{:,.2f}, Memnuniyet ortalaması {:,.2f}"
              .format(androidKullaniciOrani, androidMemnuniyetOrtalamasi))
        # genel memnuniyet hesabı
        print("Uygulamanın genel memnuniyeti: {:,.2f}".format(memnuniyetToplam / kullanicisay))
        # bir yıldan fazla kullananların değerlendirmesi
        print("Uygulamayı 1 yıldan daha uzun süre kullanan kullanıcıların sayısı: ", yilSay)
        print("Kullandıkları ortalama süre: ", yilDegerlendirme / yilSay)
        print("Memnuniyet düzeyi ortalaması: ", yilMemnun / yilSay)

        print("Uygulamadan memnun olmayan kullanıcıların uygulamayı kullandıkları ortalama süre: ",
              memnunDegilSure / memnunDegil)

        print("Uygulamanın ücretsiz kullanım süresi dolmadan silen kullanıcıların tüm kullanıcılar içindeki oranı: "
              "%{:,.2f}".format(100 * silenSayac / kullanicisay))
