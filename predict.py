import pandas as pd
import pickle

# Load model dari file
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Contoh input nilai siswa
data_baru = pd.DataFrame([{
    "Matematika": 75,
    "Bahasa Indonesia": 78,
    "IPA": 74,
    "IPS": 70
}])

# Prediksi
hasil = model.predict(data_baru)

# Tampilkan hasil
print("🎯 Hasil Prediksi Remedial:")
if hasil[0] == 1:
    print("🔴 Siswa PERLU remedial")
else:
    print("🟢 Siswa TIDAK perlu remedial")
