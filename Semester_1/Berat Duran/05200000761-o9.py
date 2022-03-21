# text içindeki büyük harf ı ları küçük harf i değil ı ya çevirir
def inputTr():
    string = input("Paragrafınızı tek satır halinde yazınız: ")
    isizString = string.replace("I", "ı").replace("İ", "i").lower()
    # örnek input alttadır.
    # 'Islak ve uzun bir yolculuktan sonra işte şimdi oradayız. Kötü amaçların güdüldüğü bir öğretmen okulundayız. Yetiştirilen öğretmenlere öğrencileri nasıl muvaffakiyetsizleştirecekleri öğretiliyor. Yani öğretmenler birer muvaffakiyetsizleştirici olarak yetiştiriliyorlar. Fakat öğretmenlerden biri muvaffakiyetsizleştirici olmayı, yani muvaffakiyetsizleştiricileştirilmeyi reddediyor, bu konuda ileri geri konuşuyor. Bütün öğretmenleri kolayca muvaffakiyetsizleştiricileştiriverebileceğini sanan okul müdürü bu duruma sinirleniyor, ve söz konusu öğretmeni makamına çağırıp ona diyor ki: "Muvaffakiyetsizleştiricileştiriveremeyebileceklerimizdenmişsinizcesine laflar ediyormuşsunuz ha?'
    return isizString


# noktalama işaretlerini textten siler
def stringiAlDuzenle(isizstring):
    noktalama = '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '\\', '’', "‘", '”', '“'
    isaretsizList = []
    isizstring = isizstring.split()
    for word in isizstring:
        for char in noktalama:
            word = word.replace(char, "")
        isaretsizList.append(word)
    return isaretsizList


# gereksiz kelimeleri textten siler
def gereksizKelimeleriEle(stringlist):
    gereksizler = ["acaba", "altmış", "altı", "ama", "ancak", "arada", "aslında", "ayrıca", "bana", "bazı", "belki",
                   "ben", "benden", "beni", "benim", "beri", "beş", "bile", "bin", "bir", "birçok", "biri", "birkaç",
                   "birkez", "birşey", "birşeyi", "biz", "bize", "bizden", "bizi", "bizim", "böyle", "böylece", "bu",
                   "buna", "bunda", "bundan", "bunlar", "bunları", "bunların", "bunu", "bunun", "burada", "çok",
                   "çünkü", "da", "daha", "dahi", "de", "defa", "değil", "diğer", "diye", "doksan", "dokuz", "dolayı",
                   "dolayısıyla", "dört", "edecek", "eden", "ederek", "edilecek", "ediliyor", "edilmesi", "ediyor",
                   "eğer", "elli", "en", "etmesi", "etti", "ettiği", "ettiğini", "gibi", "göre", "halen", "hangi",
                   "hatta", "hem", "henüz", "hep", "hepsi", "her", "herhangi", "herkesin", "hiç", "hiçbir", "için",
                   "iki", "ile", "ilgili", "ise", "işte", "itibaren", "itibariyle", "kadar", "karşın", "katrilyon",
                   "kendi", "kendilerine", "kendini", "kendisi", "kendisine", "kendisini", "kez", "ki", "kim", "kimden",
                   "kime", "kimi", "kimse", "kırk", "milyar", "milyon", "mu", "mü", "mı", "nasıl", "ne", "neden",
                   "nedenle", "nerde", "nerede", "nereye", "niye", "niçin", "o", "olan", "olarak", "oldu", "olduğu",
                   "olduğunu", "olduklarını", "olmadı", "olmadığı", "olmak", "olması", "olmayan", "olmaz", "olsa",
                   "olsun", "olup", "olur", "olursa", "oluyor", "on", "ona", "ondan", "onlar", "onlardan", "onları",
                   "onların", "onu", "onun", "otuz", "oysa", "öyle", "pek", "rağmen", "sadece", "sanki", "sekiz",
                   "seksen", "sen", "senden", "seni", "senin", "siz", "sizden", "sizi", "sizin", "şey", "şeyden",
                   "şeyi", "şeyler", "şöyle", "şu", "şuna", "şunda", "şundan", "şunları", "şunu", "tarafından",
                   "trilyon", "tüm", "üç", "üzere", "var", "vardı", "ve", "veya", "ya", "yani", "yapacak", "yapılan",
                   "yapılması", "yapıyor", "yapmak", "yaptı", "yaptığı", "yaptığını", "yaptıkları", "yedi", "yerine",
                   "yetmiş", "yine", "yirmi", "yoksa", "yüz", "zaten", "altmýþ", "altý", "bazý", "beþ", "birþey",
                   "birþeyi", "INSERmi", "kýrk", "mý", "nasýl", "onlari", "onlarýn", "yetmiþ", "þey", "þeyden", "þeyi",
                   "þeyler", "þu", "þuna", "þunda", "þundan", "þunu"]
    gerekliList = str()
    # eğer kelimeler bu listedeyse yeni oluşan liteye atmaması için blok
    for word in stringlist:
        if word not in gereksizler:
            gerekliList += word + " "

    return gerekliList


# ilk tablonun oluşturulması içindir
def ilkTabloUlustur(mystr):
    print("Kalan Metindeki Kelimeler                                                      Tekrar Sayıları")
    print("----------------------------------------------------------------------         ---------------")
    dic = {}
    # string içindeki her bir kelime için dönen ve bu kelimenin listedeki sayısını bulur
    for word in mystr:
        if word not in dic:
            dic[word] = mystr.count(word)

    for i in dic:
        print(f"{i:70}         {dic[i]:15}")


# ikinci tabloyu oluşturur
def ikinciTabloOlustur(mystr):
    lenDic = {}
    print("\nKelime Uzunluğu    Kelime Sayısı")
    print("---------------    -------------")
    lenlist = []
    for word in mystr:
        lenlist.append(len(word))
    lenlist.sort()
    # her bir uzunluk değeri kelime sayısını bulur
    for uzunluk in lenlist:
        if uzunluk not in lenDic:
            lenDic[uzunluk] = lenlist.count(uzunluk)
    for i in lenDic:
        print(f"{i:15}      {lenDic[i]:11}")


def main():
    mystr = gereksizKelimeleriEle(stringiAlDuzenle(inputTr()))
    mystr = mystr.split()

    ilkTabloUlustur(mystr)
    ikinciTabloOlustur(mystr)


main()
