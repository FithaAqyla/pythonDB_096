import sqlite3
import tkinter as tk

# Fungsi untuk menentukan prediksi berdasarkan nilai tertinggi
def prediksi():
    # Mengambil nilai dari entry
    nama = entry_nama.get()
    nilai_matematika = float(entry_matematika.get())
    nilai_inggris = float(entry_inggris.get())
    nilai_geografi = float(entry_geografi.get())

    # Menentukan prodi berdasarkan nilai tertinggi
    prodi = ""
    if nilai_matematika >= nilai_inggris and nilai_matematika >= nilai_geografi:
        prodi = "Kedokteran"
    elif nilai_matematika >=nilai_matematika and nilai_geografi >= nilai_inggris:
        prodi = "Teknik"
    elif nilai_inggris >= nilai_geografi and nilai_inggris >= nilai_matematika:
        prodi = "Pendidikan"

    # Menampilkan hasil prediksi
    label_hasil.config(text=f"Hasil Prediksi untuk {nama}: {prodi}")

    # Simpan data ke database SQLite
    conn = sqlite3.connect('prodi.db')
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        matematika REAL,
                        inggris REAL,
                        geografi REAL,
                        prediksi_fakultas TEXT
                    )''')

    # Menyimpan nilai siswa ke dalam database
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, matematika, inggris, geografi, prediksi_fakultas)
                      VALUES (?, ?, ?, ?, ?)''', (nama, nilai_matematika, nilai_inggris, nilai_geografi, prodi))
    
    conn.commit()
    conn.close()

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

label_judul = tk.Label(root, text="Aplikasi prediksi Prodi Pilihan")
label_judul.pack()

label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label_matematika = tk.Label(root, text="Nilai matematika:")
label_matematika.pack()
entry_matematika = tk.Entry(root)
entry_matematika.pack()

label_inggris = tk.Label(root, text="Nilai inggris:")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

label_geografi = tk.Label(root, text="Nilai geografi:")
label_geografi.pack()
entry_geografi = tk.Entry(root)
entry_geografi.pack()

button_prediksi = tk.Button(root, text="Hasil Prediksi", command=prediksi)
button_prediksi.pack()

label_hasil = tk.Label(root, text="")
label_hasil.pack()

root.mainloop()