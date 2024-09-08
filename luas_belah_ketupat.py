import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung luas belah ketupat
def hitung_luas():
    try:
        # Ambil input dari kotak input dan ubah ke tipe float
        diagonal1 = float(entry_diagonal1.get())
        diagonal2 = float(entry_diagonal2.get())
        
        # Hitung luas belah ketupat (1/2 * diagonal1 * diagonal2)
        luas = 0.5 * diagonal1 * diagonal2
        
        # Tampilkan hasilnya di label hasil
        label_hasil.config(text=f"Luas Belah Ketupat: {luas} unit²")
    except ValueError:
        # Jika input bukan angka, tampilkan pesan error
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid untuk kedua diagonal!")

# Membuat jendela utama
window = tk.Tk()
window.title("Fara Azzura Dasgupta | Luas Belah Ketupat")

# Ukuran jendela
window.geometry("400x200")

# Membuat label dan entry untuk diagonal pertama
label_diagonal1 = tk.Label(window, text="Masukkan Diagonal 1:")
label_diagonal1.pack(pady=5)
entry_diagonal1 = tk.Entry(window)
entry_diagonal1.pack(pady=5)

# Membuat label dan entry untuk diagonal kedua
label_diagonal2 = tk.Label(window, text="Masukkan Diagonal 2:")
label_diagonal2.pack(pady=5)
entry_diagonal2 = tk.Entry(window)
entry_diagonal2.pack(pady=5)

# Membuat tombol untuk menghitung luas
button_hitung = tk.Button(window, text="Hitung Luas", command=hitung_luas)
button_hitung.pack(pady=10)

# Membuat label untuk menampilkan hasil
label_hasil = tk.Label(window, text="")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
window.mainloop()