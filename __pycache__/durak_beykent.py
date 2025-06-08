# durak_beylikduzu_son_durak.py

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

beykent = Durak("Beykent")
