"""
Program menghitung luas segitiga
luas segitiga = alas * tinggi / 2
"""
print('Menghitung Luas Segitiga')
alas = 7
tinggi = 10
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dgn alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMenghitung Luas Segitiga dengan copy paste')
alas = 8
tinggi = 10
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dgn alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')


def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga


print(' ')
print(hitung_luas_segitiga(10, 2))
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10, 6)}')
