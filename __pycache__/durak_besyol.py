import random

class Durak:
    def __init__(self, ad):
        self.ad = ad
        self.kamera = None

    def kamera_ekle(self, kamera):
        self.kamera = kamera

    def kamera_kaydi_al(self, metrobus):
        if self.kamera:
            self.kamera.kaydi_al(metrobus)
        else:
            print(f"[UYARI] {self.ad} durağında kamera yok!")

    def yolcu_sayisini_uret(self):
        return random.randint(20, 120)

    def sefer_gerekli_mi(self):
        return self.yolcu_sayisi > 70

besyol = Durak("Beşyol")