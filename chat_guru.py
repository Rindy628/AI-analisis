def konsultasi_guru(pertanyaan):
    pertanyaan = pertanyaan.lower()

    if "remedial ipa" in pertanyaan:
        return """📚 *Materi Remedial IPA*:
- Ekosistem (rantai makanan, interaksi makhluk hidup)
- Energi dan perubahannya (konduksi, konveksi, radiasi)
- Sifat zat dan perubahannya

🎯 Fokus Pembelajaran: eksperimen sederhana dan konsep dasar

🧪 Tips: gunakan media visual seperti gambar alur rantai makanan, atau percobaan mini di kelas

🔎 Info tambahan: https://www.google.com/search?q=materi+remedial+IPA"""

    elif "remedial matematika" in pertanyaan:
        return """📚 *Materi Remedial Matematika*:
- Operasi bilangan pecahan
- Perbandingan dan skala
- Aljabar dasar

🎯 Fokus Pembelajaran: latihan step-by-step dan soal kontekstual

🧪 Tips: gunakan alat peraga dan gamifikasi latihan

🔎 Info tambahan: https://www.google.com/search?q=materi+remedial+matematika"""

    elif "remedial bahasa indonesia" in pertanyaan:
        return """📚 *Materi Remedial Bahasa Indonesia*:
- Ide pokok dan kalimat utama
- Struktur teks narasi, eksplanasi, dan laporan
- Kata baku dan tidak baku

🎯 Fokus Pembelajaran: latihan memahami teks pendek dan mencari kalimat utama

🧪 Tips: gunakan metode "Tanya-Jawab Terbalik" (siswa bikin soal dari teks)

🔎 Info tambahan: https://www.google.com/search?q=materi+remedial+bahasa+indonesia"""

    elif "remedial ips" in pertanyaan:
        return """📚 *Materi Remedial IPS*:
- Interaksi sosial dan norma
- Keragaman budaya Indonesia
- Letak geografis dan pengaruhnya

🎯 Fokus Pembelajaran: koneksi materi dengan kehidupan sehari-hari

🧪 Tips: gunakan peta interaktif atau studi kasus lokal

🔎 Info tambahan: https://www.google.com/search?q=materi+remedial+ips"""

    elif "tips belajar siswa" in pertanyaan:
        return """🎓 *Tips Meningkatkan Pembelajaran Siswa*:
- Gunakan metode visual-auditori-kinestetik
- Lakukan evaluasi per topik, bukan per bab
- Berikan feedback personal

🔎 Info tambahan: https://www.google.com/search?q=metode+belajar+efektif+untuk+siswa"""

    elif "cara mengajar" in pertanyaan:
        return """👩‍🏫 *Strategi Mengajar yang Menarik*:
- Mulai pelajaran dengan pertanyaan pancingan
- Gunakan studi kasus nyata
- Terapkan pembelajaran kooperatif (kelompok kecil)

🔎 Info tambahan: https://www.google.com/search?q=strategi+mengajar+efektif"""

    elif "penyebab siswa remedial" in pertanyaan:
        return """🚨 *Faktor Penyebab Siswa Remedial*:
- Gaya belajar tidak sesuai
- Kurangnya latihan/latih soal
- Beban materi terlalu cepat

🧪 Solusi: deteksi sejak awal lewat pretest dan diagnosis kesulitan

🔎 Info tambahan: https://www.google.com/search?q=penyebab+siswa+remedial"""

    else:
        return """❓ Maaf kapten, budakmu belum bisa jawab pertanyaan itu sekarang.
Coba ketik dengan lebih spesifik yaa.

🔎 Atau cek info manual: https://www.google.com/search?q=""" + pertanyaan.replace(" ", "+")

