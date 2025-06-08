import metrobus


class Metrobus_Filosu:
    def __init__(self):
        self.metrobusler = []

    def Metrobus_Filosuna_Ekle(self, metrobus):
        self.metrobusler.append(metrobus)

    def filo_goster(self):
        for i in self.metrobusler:
            print('{} nolu {} plakalı  {} hangarda {} vaziyetindedir'.format(i.metrobus_id, i.metrobus_plaka, i.metrobus_turu, i.koordinat,i.durum))


filo = Metrobus_Filosu()
filo.Metrobus_Filosuna_Ekle(metrobus.m1)
filo.Metrobus_Filosuna_Ekle(metrobus.m2)
filo.Metrobus_Filosuna_Ekle(metrobus.m3)
filo.Metrobus_Filosuna_Ekle(metrobus.m4)
filo.Metrobus_Filosuna_Ekle(metrobus.m5)
filo.Metrobus_Filosuna_Ekle(metrobus.m6)
filo.Metrobus_Filosuna_Ekle(metrobus.m7)
filo.Metrobus_Filosuna_Ekle(metrobus.m8)
filo.Metrobus_Filosuna_Ekle(metrobus.m9)
filo.Metrobus_Filosuna_Ekle(metrobus.m10)
filo.Metrobus_Filosuna_Ekle(metrobus.m11)
filo.Metrobus_Filosuna_Ekle(metrobus.m12)
filo.Metrobus_Filosuna_Ekle(metrobus.m13)
filo.Metrobus_Filosuna_Ekle(metrobus.m14)
filo.Metrobus_Filosuna_Ekle(metrobus.m15)
filo.Metrobus_Filosuna_Ekle(metrobus.m16)
filo.Metrobus_Filosuna_Ekle(metrobus.m17)
filo.Metrobus_Filosuna_Ekle(metrobus.m18)
filo.Metrobus_Filosuna_Ekle(metrobus.m19)
filo.Metrobus_Filosuna_Ekle(metrobus.m20)

