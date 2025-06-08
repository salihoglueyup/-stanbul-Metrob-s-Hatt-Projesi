varsayilan_guzergah_adlari = [
    "Beylikdüzü Son Durak",
    "Beykent",
    "Cumhuriyet Mahallesi",
    "Beylikdüzü Belediyesi",
    "Beylikdüzü",
    "Güzelyurt",
    "Haramidere",
    "Haramidere Sanayi",
    "Saadetdere Mahallesi",
    "Mustafa Kemal Paşa",
    "Cihangir-Üniversite Mahallesi",
    "Avcılar Merkez Üniversite Kampüsü",
    "Şükrübey",
    "Büyükşehir Belediyesi Sosyal Tesisleri",
    "Küçükçekmece",
    "Cennet Mahallesi",
    "Florya",
    "Beşyol",
    "Sefaköy",
    "Yenibosna",
    "Şirinevler",
    "Bahçelievler",
    "İncirli",
    "Zeytinburnu",
    "Merter",
    "Cevizlibağ",
    "Topkapı-Şehit Mustafa Cambaz",
    "Bayrampaşa-Maltepe"
    "Edirnekapı"
    "Ayvansaray-Eyüp Sultan"
    "Halıcıoğlu"
    "Okmeydanı"
    "Darülaceze - Perpa"
    "Okmeydanı Hastane"
    "Çağlayan"
    "Mecidiyeköy"
    "Zincirlikuyu"
    "15 Temmuz Şehitler Köprüsü"
    "Burhaniye"
    "Altunizade"
    "Acıbadem"
    "Uzunçayır"
    "Fikirtepe"
    "Söğütlüçeşme"
]

def rota_olustur(tum_duraklar, guzergah_adlari):
    rota = []
    for ad in guzergah_adlari:
        for d in tum_duraklar:
            if d.ad == ad:
                rota.append(d)
                break
    return rota

def hedefe_kadar_guzergah(rota, hedef_durak):
    g = []
    for d in rota:
        g.append(d)
        if d.ad == hedef_durak.ad:
            break
    return g
