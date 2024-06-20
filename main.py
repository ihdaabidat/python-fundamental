"""Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekunsial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""


# Sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1678
print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi berjalan ke rak botol susu")
    print("Budi membeli 1 botol susu")
else:
    print("Budi tidak membeli 1 botol susu")

if jumlah_telur > 0:
    print("Budi mengecek apakah ada telur, dan ternyata telurnya ada")
    print("Budi membeli 6 butir telur")
else:
    print("Budi tidak membeli 6 butir telur")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")

