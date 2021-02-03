from geometri.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'ini adalah objek dari segitiga dengan alas = {self.alas} cm, dan tinggi = {self.tinggi} cm'

    def hitung_luas(self):
        return self.alas * self.tinggi / 2