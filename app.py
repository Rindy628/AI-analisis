from flask import Flask, render_template, request, send_file
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 🔍 Analisis untuk nilai akhir (komponen penilaian)
def analisis_remedial(df, kkm_dict):
    hasil = []
    for index, row in df.iterrows():
        nama = row['Nama']
        remed_mapel = []
        for mapel in kkm_dict:
            nilai = row.get(mapel, 0)
            if pd.notna(nilai) and nilai < kkm_dict[mapel]:
                remed_mapel.append((mapel, nilai, kkm_dict[mapel]))
        if remed_mapel:
            hasil.append({
                'nama': nama,
                'remedial': remed_mapel
            })
    return hasil

# 🔍 Analisis untuk nilai harian
def analisis_nilai_harian_ai(df, form_data):
    total_siswa = len(df)
    tugas_cols = [col for col in df.columns if col.lower().startswith('tugas')]

    gagal_tugas = {}

    for col in tugas_cols:
        jumlah_gagal = df[df[col] < 75].shape[0]
        gagal_tugas[col] = jumlah_gagal

    if not gagal_tugas:
        return "Semua siswa lulus semua tugas."

    # Cari tugas yang paling banyak gagal
    tugas_terbanyak = max(gagal_tugas, key=gagal_tugas.get)
    jumlah_gagal = gagal_tugas[tugas_terbanyak]
    persen = (jumlah_gagal / total_siswa) * 100

    # Ambil nomor tugas (misal Tugas2 => 2)
    tugas_num = ''.join(filter(str.isdigit, tugas_terbanyak))
    form_field = f"materi{tugas_num}"
    materi = form_data.get(form_field, f"Materi {tugas_num}")

    hasil_analisis = (
        f"Dari {total_siswa} siswa, {jumlah_gagal} siswa atau {persen:.0f}% "
        f"mengalami kesulitan di {tugas_terbanyak}. "
        f"AI menyarankan penguatan pada materi: {materi}."
    )
    return hasil_analisis



    # Ambil angka tugas untuk mapping ke form materi
    tugas_num = ''.join(filter(str.isdigit, tugas_terbanyak))
    form_field = f"materi{tugas_num}"
    materi = request.form.get(form_field, f"Materi {tugas_num}")

    hasil_analisis = f"Dari {total_siswa} siswa, {persen:.0f}% mengalami kesulitan di {tugas_terbanyak}. AI menyarankan penguatan pada materi: {materi}."
    return hasil_analisis


# 🔸 Halaman utama
@app.route('/')
def halaman_awal():
    return render_template('halaman_awal.html')

# 🔸 Proses upload nilai akhir
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    excel_file = pd.ExcelFile(filepath)
    df_nilai = excel_file.parse(sheet_name='komponenpenilaian')
    df_kkm = excel_file.parse(sheet_name='kkm', header=None)

    kkm_dict_excel = {}
    for i in range(len(df_kkm)):
        mapel = str(df_kkm.iloc[i, 0]).strip()
        kkm = df_kkm.iloc[i, 1]
        if pd.notna(mapel) and pd.notna(kkm):
            kkm_dict_excel[mapel] = int(kkm)

    kkm_dict = {}
    for mapel in kkm_dict_excel:
        field_name = f'kkm_{mapel.lower().replace(" ", "_")}'
        kkm_val = request.form.get(field_name)
        if kkm_val:
            try:
                kkm_dict[mapel] = int(kkm_val)
            except ValueError:
                kkm_dict[mapel] = kkm_dict_excel[mapel]
        else:
            kkm_dict[mapel] = kkm_dict_excel[mapel]

    hasil = analisis_remedial(df_nilai, kkm_dict)
    return render_template('hasil.html', hasil=hasil, kkm=kkm_dict)

# 🔸 Proses upload dan analisis nilai harian
@app.route('/analisis-nilai-harian', methods=['GET', 'POST'])
def analisis_nilai_harian():
    if request.method == 'POST':
        if 'nilai_excel' not in request.files:
            return 'No file uploaded'
        file = request.files['nilai_excel']
        if file.filename == '':
            return 'No selected file'

        df = pd.read_excel(file)
        hasil_ai = analisis_nilai_harian_ai(df, request.form)
        return render_template('hasil_nilai_harian.html', hasil_analisis=hasil_ai)
    
    return render_template('nilai_harian.html')

# 🔸 Download template nilai akhir
@app.route('/download-template')
def download_template():
    return send_file('template_nilai_akhir.xlsx', as_attachment=True)

# 🔸 Download template nilai harian
@app.route('/download-template-harian')
def download_template_harian():
    file_path = os.path.join('static', 'template_nilai_harian.xlsx')
    return send_file(file_path, as_attachment=True)





# 🔸 Halaman nilai akhir
@app.route('/index')
def index():
    return render_template('index.html')



# 🔥 Jalankan
if __name__ == '__main__':
    # app.run(debug=True)
