import tkinter as tk
from tkinter import messagebox
import math

# Fungsi untuk menghitung luas permukaan tabung
def hitung_luas():
    try:
        # Ambil input dari kotak input dan ubah ke tipe float
        radius = float(entry_radius.get())
        height = float(entry_height.get())
        
        # Hitung luas permukaan tabung
        luas = 2 * math.pi * radius * (radius + height)
        
        # Tampilkan hasilnya di label hasil
        label_hasil.config(text=f"Luas Permukaan Tabung: {luas:.2f} unit²")
    except ValueError:
        # Jika input bukan angka, tampilkan pesan error
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid untuk jari-jari dan tinggi!")

# Membuat jendela utama
window = tk.Tk()
window.title("Fara Azzura Dasgupta | Luas Tabung")

# Ukuran jendela
window.geometry("400x250")

# Membuat label dan entry untuk jari-jari
label_radius = tk.Label(window, text="Masukkan Jari-jari (r):")
label_radius.pack(pady=5)
entry_radius = tk.Entry(window)
entry_radius.pack(pady=5)

# Membuat label dan entry untuk tinggi tabung
label_height = tk.Label(window, text="Masukkan Tinggi (t):")
label_height.pack(pady=5)
entry_height = tk.Entry(window)
entry_height.pack(pady=5)

# Membuat tombol untuk menghitung luas
button_hitung = tk.Button(window, text="Hitung Luas", command=hitung_luas)
button_hitung.pack(pady=10)

# Membuat label untuk menampilkan hasil
label_hasil = tk.Label(window, text="")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
window.mainloop()