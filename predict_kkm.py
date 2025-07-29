nilai_siswa = {
    "Matematika": 75,
    "Bahasa Indonesia": 78,
    "IPA": 74,
    "IPS": 70
}

# KKM tiap mapel
kkm = {
    "Matematika": 78,
    "Bahasa Indonesia": 75,
    "IPA": 75,
    "IPS": 74
}

# Cek remedial
remedial_mapel = []
for mapel, nilai in nilai_siswa.items():
    if nilai < kkm[mapel]:
        remedial_mapel.append(mapel)

# Tampilkan hasil
print("📋 Hasil Pengecekan Remedial Berdasarkan KKM:")
if remedial_mapel:
    print("🔴 Siswa perlu remedial di mata pelajaran:")
    for mapel in remedial_mapel:
        print(f" - {mapel}")
else:
    print("🟢 Siswa TIDAK perlu remedial di semua mata pelajaran.")
