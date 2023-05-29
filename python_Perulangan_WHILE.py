# Perulangan dengan WHILE
jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jml_buku_yg_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jml_buku_yg_dibaca}')

while jml_buku_yg_dibaca < jumlah_buku:
    jml_buku_yg_dibaca = jml_buku_yg_dibaca + 1
    print(f"Buku ke {jml_buku_yg_dibaca} sudah dibaca")

print(f'Jumlah buku yang sudah dibaca {jml_buku_yg_dibaca}')
