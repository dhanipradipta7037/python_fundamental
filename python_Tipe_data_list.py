daftar_buku = ['psikologi money', 'kaizen', 'forex trading', 'psikologi kerja']

print("Menampilkan variabel daftar buku")
print(daftar_buku)

print("\nMenampilkan variabel daftar buku dengan FOR IN")
for buku in daftar_buku:
    print(buku)

print("\nMenampilkan variabel daftar buku dengan INDEKS")
print(daftar_buku[0])

print("\nMenampilkan variabel daftar buku dengan FOR IN RANGE")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku1 = [1, 'investasi saham', 777, 1000]
print("\nMenampilkan variabel daftar buku dengan FOR IN RANGE. Dimana tipe data tiap elemen berbeda")
for i in range(0, len(daftar_buku1)):
    print(daftar_buku1[i])

print("\nMenambahkan item baru ke varibel data list")
daftar_buku.append('fisika')
print(daftar_buku)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMenghapus data list dengan Clear List")
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMengganti elemen pada data list")
daftar_buku = ['psikologi money', 'kaizen', 'forex trading', 'psikologi kerja']
daftar_buku[0] = 'naruto'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMemindahkan 1 elemen pada variabel data list ke variabel lainnya")
item = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMenampilkan item yang di pindahkan tadi")
print(item)

print("\nMenghapus element dengan DEL pada variabel data list")
daftar_buku = ['psikologi money', 'kaizen', 'forex trading', 'psikologi kerja']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['psikologi money', 'kaizen', 'forex trading', 'psikologi kerja']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension START')
daftar_buku = ['psikologi money', 'kaizen', 'forex trading', 'psikologi kerja']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])






