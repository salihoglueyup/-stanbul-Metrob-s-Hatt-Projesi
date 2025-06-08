from datetime import datetime

class Kamera:
    def __init__(self, kamera_id, izlenen_durak):
        self.kamera_id = kamera_id
        self.izlenen_durak = izlenen_durak

    def kontrol_et(self):
        self.izlenen_durak.yolcu_sayisini_uret()
        yolcu_sayisi = self.izlenen_durak.yolcu_sayisi
        mesaj = ""

        if yolcu_sayisi > 50:
            mesaj = f"⛔️ Kamera {self.kamera_id}: {self.izlenen_durak.ad} → {yolcu_sayisi} yolcu. Sefer gerekli."
            karar = True
        else:
            mesaj = f"🟢 Kamera {self.kamera_id}: {self.izlenen_durak.ad} → {yolcu_sayisi} yolcu. Sefer gerekmez."
            karar = False

        print(mesaj)
        self.log_yaz(mesaj)
        return karar

    def kayit_al(self, metrobus):
        saat = datetime.now().strftime("%H:%M")
        mesaj = f"[{saat}] Kamera {self.kamera_id} → {metrobus.metrobus_id} ({metrobus.metrobus_plaka}) araci {self.izlenen_durak.ad} durağından geçti."
        print(mesaj)
        self.log_yaz(mesaj)

    def log_yaz(self, mesaj):
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_satiri = f"[{zaman}] {mesaj}\n"
        with open("kamera_log.txt", "a", encoding="utf-8") as dosya:
            dosya.write(log_satiri)
