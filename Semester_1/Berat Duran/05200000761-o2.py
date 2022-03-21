# COVID-19 (+) bir kişi ile son 48 saat içerisinde aynı ortamda bulunmuş olan bir kişi, bu kişi
# ile aynı ortamda maskesiz olarak 1 metreden daha yakın mesafede 15 dk veya daha uzun süre
# bulunduysa “yakın temaslı”, diğer durumda ise “temaslı” olarak nitelendirilmektedir. Ayrıca
# yakın temaslı olan ve/veya ağır kronik hastalığı olan kişilere tedbir amaçlı ilaç tedavisi
# verilmektedir.


aradakiMesafe = 0
gecenSure = 0  # ilk tanım aşaması if içinde olduğu için objeyi baslangicta olusturuyoruz
temasGrubu = ''
mesafe = 100  # hasta yankıdında yakın temaslı olabilmek için gereken mesafe
minsure = 15  # hasta yakınında yakın temaslı olabilmek için gerekli min süre
adSoyad = input("Adınızı ve soyadınızı giriniz: ")
maskeKontrol = input("COVID-19 (+) kişi ile temas ettiğiniz sırada maske takıp takmadığınızı giriniz (e/h):")


if maskeKontrol == 'h':     # maske kontrolü aşaması
    aradakiMesafe = int(input("COVID-19 (+) kişi ile temas ettiğiniz sırada aranızda ne kadar mesafe vardı: "))
    gecenSure = int(input("COVID-19 (+) kişi ile bu mesafede ne kadar süre geçirdiniz: "))
else:       # Kullanıcı e veya h dışında değer girmeyeceği için else ile devam edildi
    print("Sayın " + adSoyad + ',\nMaske taktığınız için teşekkürler.')      # Kendi output eklemem


kronikHastalik = input("Ağır kronik bir hastalığınız olup olmadığını giriniz (e/h):")
    

if aradakiMesafe < mesafe and gecenSure >= minsure:    # hem aradaki mesafe hem de gecen süreye göre temas grubu ataması
    temasGrubu = "Yakın temaslı"        # str kısa bir str olmasa da print içinde de kullanılması içindir
else:
    temasGrubu = "Temaslı"


print('Sayın ' + adSoyad + ',\n' + temasGrubu + ' grubundasınız.')      # istenen çıktılar arasındaki grup çıktısı
if kronikHastalik == 'e' or temasGrubu == 'Yakın temaslı':       # hem kronik hastalık hem de yakın temas ilaç sebebidir
    print("İlaç tedavisi almanıza gerek vardır.")                       # istenen çıktıalr arasındaki ilaç alımı çıktısı
else:
    print("İlaç tedavisi almanıza gerek yoktur.")
