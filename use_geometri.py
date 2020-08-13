# from geometri.persegipanjang import luas_persegi_panjang
#from geometri.segitiga import hitung_luas_segitiga
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga
from geometri.persegipanjang import luas_persegi_panjang, info as info_persegipanjang

print(info_segitiga())
print(f'luasnya {hitung_luas_segitiga(10, 5)}')

print(info_persegipanjang())
print(f'luasnya {luas_persegi_panjang(10, 5)}')
