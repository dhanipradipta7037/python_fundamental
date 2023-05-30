# Perulangan dengan WHILE sampai paham
jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jml_buku_yg_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {jml_buku_yg_dibaca_dan_dipahami}')

total_jml_baca = 0

while total_jml_baca < jumlah_buku * 2:
    total_jml_baca = total_jml_baca + 1
    if jml_buku_yg_dibaca_dan_dipahami == 9:
        print(f"Buku ke {jml_buku_yg_dibaca_dan_dipahami + 1} belum paham")
    else:
        jml_buku_yg_dibaca_dan_dipahami = jml_buku_yg_dibaca_dan_dipahami + 1
        print(f"Buku ke {jml_buku_yg_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f'Jumlah buku yang sudah dibaca dan dipahami hanya {jml_buku_yg_dibaca_dan_dipahami}')

if jml_buku_yg_dibaca_dan_dipahami == jumlah_buku:
    print("Bu, semua buku sudah dibaca dan dipahami")
else:
    print(f"Bu, tidak semua buku bisa dipahami. "
          f"Budi hanya bisa memahami {jml_buku_yg_dibaca_dan_dipahami}")

