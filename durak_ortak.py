import random

class Durak:
    def __init__(self, ad):
        self.ad = ad
        self.kamera = None
        self.yolcu_sayisi = self.yolcu_sayisini_uret()

    def kamera_ekle(self, kamera):
        self.kamera = kamera

    def yolcu_sayisini_uret(self):
        self.yolcu_sayisi = random.randint(20, 120)

    def sefer_gerekli_mi(self):
        return self.yolcu_sayisi > 70
