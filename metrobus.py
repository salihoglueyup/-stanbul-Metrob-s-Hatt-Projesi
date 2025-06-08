import time
from datetime import datetime


class Metrobus:
    def __init__(self, metrobus_id, metrobus_plaka, metrobus_turu):
        self.metrobus_id = metrobus_id
        self.metrobus_plaka = metrobus_plaka
        self.metrobus_turu = metrobus_turu
        self.durum = 'bekleme'
        self.koordinat = (0, 0, 0)

    def koordinata_git(self, x, y, z):
        self.koordinat = (x, y, z)

    def metrobus_bilgisi(self):
        print('{} nolu {} plakalı {} koordinatta {} vaziyetindedir'.format(self.metrobus_id, self.metrobus_plaka,self.metrobus_turu, self.durum))

    def sefere_basla(self, guzergah):
        if self.durum == "seferde":
            print(f"{self.metrobus_id} zaten seferde!")
            return
        self.guzergah = guzergah
        self.aktif_durak_index = 0
        self.durum = "seferde"
        print(f"{self.metrobus_id} seferine başladı.")
        self.seferi_baslat()

    def seferi_baslat(self):
        while self.aktif_durak_index < len(self.guzergah):
            durak = self.guzergah[self.aktif_durak_index]
            saat = datetime.now().strftime("%H:%M")
            print(f"[{saat}] {self.metrobus_id} → {durak.ad} durağında.")
            if hasattr(durak, "kamera") and durak.kamera is not None:
                durak.kamera.kayit_al(self)
            self.aktif_durak_index += 1
            time.sleep(1)
        print(f"{self.metrobus_id} seferini tamamladı.")
        self.durum = "beklemede"


m1 = Metrobus('M1', '34 TR 7109', 'Otokar Kent XL')
m2 = Metrobus('M2', '34 GPA 220', 'Otokar Kent XL')
m3 = Metrobus('M3', '34 AA 2375', 'Otokar Kent XL')
m4 = Metrobus('M4', '34 FHK 672', 'Otokar Kent XL')
m5 = Metrobus('M5', '34 HKL 443', 'Otokar Kent XL')
m6 = Metrobus('M6', '34 UO 1420', 'Mercedes Capacity')
m7 = Metrobus('M7', '34 HKS 616', 'Mercedes Capacity')
m8 = Metrobus('M8', '34 CBN 257', 'Mercedes Capacity')
m9 = Metrobus('M9', '34 ASD 891', 'Mercedes Capacity')
m10 = Metrobus('M10', '34 MKS 359', 'Mercedes Capacity')
m11 = Metrobus('M11', '34 ERT 522', 'Mercedes Conecto')
m12 = Metrobus('M12', '34 RNG 987', 'Mercedes Conecto')
m13 = Metrobus('M13', '34 BNO 658', 'Mercedes Conecto')
m14 = Metrobus('M14', '61 EYP 611', 'Mercedes Conecto')
m15 = Metrobus('M15', '34 SDG 547', 'Mercedes Conecto')
m16 = Metrobus('M16', '61 EZS 346', 'Akia Ultra LF 25')
m17 = Metrobus('M17', '34 PKN 142', 'Akia Ultra LF 25')
m18 = Metrobus('M18', '34 TN 1728', 'Akia Ultra LF 25')
m19 = Metrobus('M19', '34 FK 3570', 'Akia Ultra LF 25')
m20 = Metrobus('M20', '34 SSS 398', 'Akia Ultra LF 25')
