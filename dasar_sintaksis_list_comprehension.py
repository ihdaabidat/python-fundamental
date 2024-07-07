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

print('\nMembuat list baru')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# meskipun daftar_buku dihapus tapi daftar_buku_baru itu sudah menjadi list yang terpisah sehingga dia ga akan terpengaruh (tempatnya udah berbeda)
print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# meskipun daftar_buku dihapus tapi daftar_buku_baru itu sudah menjadi list yang terpisah sehingga dia ga akan terpengaruh (tempatnya udah berbeda)
print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])
