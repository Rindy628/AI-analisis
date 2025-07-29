import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os

# Baca file Excel
df = pd.read_excel("data/nilai_siswa.xlsx")

# Hitung rata-rata nilai
df["Rata-rata"] = df[["Matematika", "Bahasa Indonesia", "IPA", "IPS"]].mean(axis=1)

# Tambahin kolom label: 1 = remedial, 0 = tidak
df["Remedial"] = df["Rata-rata"].apply(lambda x: 1 if x < 70 else 0)

# Fitur (X) dan Label (y)
X = df[["Matematika", "Bahasa Indonesia", "IPA", "IPS"]]
y = df["Remedial"]

# Buat model KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Simpan model ke folder models/
os.makedirs("models", exist_ok=True)
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model berhasil dilatih dan disimpan di models/model.pkl")
