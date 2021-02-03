from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        # fungsi yang dipanggil pertama kali saat objek diciptakan
        self.p = p
        self.l = l

    def info(self):
        return f'ini adalah objek dari PersegiPanjang dengan panjang = {self.p} cm, dan lebar = {self.l} cm'

    def hitung_luas(self):
        return self.p * self.l
