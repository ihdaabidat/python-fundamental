## Operasi Dasar List ##

### Memahami dan Menggunakan List ####
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
print('Tampilkan variable daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Volume 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda-beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
print('Tambahkan 1 buku baru')
daftar_buku.append('Dunia Matemaika Kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nVariabel yang sering di pake i, j, k')

print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

### Menggunakan List Comprehension ###
print('\nPerintah del dengan List comprehension')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan List comprehension start')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0:3] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan List comprehension start -1')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0:-2] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan List comprehension start:end:step')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First']
del daftar_buku[0::2] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan List comprehension start:end:step')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First']
del daftar_buku[0::2] #START:END:STEPPPP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

