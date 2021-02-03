from geometri.bangun_ruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('penggunaan oop')
p1 = PersegiPanjang(20, 4)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(20, 4)
print(s1.info())
print(s1.hitung_luas())

print('\nmencoba membuat objek dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\npolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
