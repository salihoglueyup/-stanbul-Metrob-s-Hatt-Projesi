import os
import importlib
import random
import time
from metrobus_filosu import filo
from nvr import Kamera
from guzergah import varsayilan_guzergah_adlari, rota_olustur, hedefe_kadar_guzergah

print("\n📡 Metrobüs Güzergah Simülasyonu Başladı\n")

duraklar = []
for dosya in os.listdir("duraklar"):
    if dosya.endswith(".py") and dosya != "__init__.py":
        modul_adi = dosya[:-3]
        modul = importlib.import_module(f"duraklar.{modul_adi}")
        durak = getattr(modul, "durak")
        kamera = Kamera(kamera_id=f"K-{durak.ad.replace(' ', '_')}", izlenen_durak=durak)
        durak.kamera = kamera
        duraklar.append(durak)

rota = rota_olustur(duraklar, varsayilan_guzergah_adlari)

print("\n📋 Mevcut Filodaki Araçlar:\n")
filo.filo_goster()

print("\n🟢 Boşta Olan Araçlar:")
for m in filo.metrobusler:
    if m.durum == "beklemede":
        print(f"   {m.metrobus_id} → boşta")

print("\n🔴 Aktif Seferde Olan Araçlar:")
for m in filo.metrobusler:
    if m.durum == "seferde":
        print(f"   {m.metrobus_id} → seferde")

for hedef_durak in rota:

    if hedef_durak.kamera:
        sefer_gerekli = hedef_durak.kamera.kontrol_et()
    else:
        sefer_gerekli = hedef_durak.sefer_gerekli_mi()

    if sefer_gerekli:
        uygun_araclar = [m for m in filo.metrobusler if m.durum != "seferde"]

        if uygun_araclar:
            secilen = random.choice(uygun_araclar)
            guzergah = hedefe_kadar_guzergah(rota, hedef_durak)

            print(f"\n🚌 {secilen.metrobus_id} → {hedef_durak.ad} için kalkıyor.")
            print(f"🗺️ Güzergah:")
            for d in guzergah:
                print(f"   → {d.ad}")

            secilen.sefere_basla(guzergah)
            time.sleep(1)
        else:
            print("🚫 Müsait araç yok. Sefer atanamadı.")
    else:
        print("🟢 Sefer gerekmez.")

