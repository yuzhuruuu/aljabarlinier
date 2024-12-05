#PROGRAM UNTUK MEMBUAT MATRIKS MENJADI MATRIKS ESELON BARIS TEREDUKSI-REVISI

import tkinter as tk
from tkinter import messagebox
import numpy as np

def buat_matriks():
    try:
        nrows = int(input_rows.get())
        ncols = int(input_cols.get())
        
        # Buat grid input matriks
        global entries
        entries = [[None for _ in range(ncols)] for _ in range(nrows)]
        
        # Hapus grid sebelumnya jika ada
        for widget in frame_matriks.winfo_children():
            widget.destroy()
        
        # Buat grid input matriks
        for i in range(nrows):
            for j in range(ncols):
                entries[i][j] = tk.Entry(frame_matriks, width=5)
                entries[i][j].grid(row=i, column=j, padx=5, pady=5)
        
        # Pastikan tombol ditampilkan di bawah grid
        btn_selesaikan.pack(pady=10)
    except ValueError:
        messagebox.showerror("Error", "Masukkan ukuran baris dan kolom yang valid!")

def row_echelon_form(matrix):
    nrows, ncols = matrix.shape
    lead = 0

    for r in range(nrows):
        if lead >= ncols:
            break

        i = r
        while matrix[i, lead] == 0:
            i += 1
            if i == nrows:
                i = r
                lead += 1
                if lead == ncols:
                    break

        if lead >= ncols:
            break

        matrix[[r, i]] = matrix[[i, r]]

        if matrix[r, lead] != 0:
            matrix[r] = matrix[r] / matrix[r, lead]

        for i in range(nrows):
            if i != r:
                ratio = matrix[i, lead]
                matrix[i] = matrix[i] - ratio * matrix[r]

        lead += 1

    return matrix

def selesaikan():
    try:
        nrows = int(input_rows.get())
        ncols = int(input_cols.get())
        
        # Ambil input matriks dari grid
        matrix = np.zeros((nrows, ncols), dtype=float)
        for i in range(nrows):
            for j in range(ncols):
                matrix[i, j] = float(entries[i][j].get())
        
        # Proses matriks menjadi eselon baris tereduksi
        result = row_echelon_form(matrix)
        
        # Tampilkan hasil
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Matrix dalam bentuk eselon baris tereduksi:\n")
        for row in result:
            output.insert(tk.END, f"{row}\n")
    except ValueError:
        messagebox.showerror("Error", "Masukkan elemen matriks yang valid!")

# GUI
root = tk.Tk()
root.title("Matriks Eselon Baris Tereduksi")

# Input untuk ukuran matriks
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Masukkan ukuran matriks").grid(row=0, column=0, columnspan=2)
tk.Label(frame_input, text="Baris:").grid(row=1, column=0)
input_rows = tk.Entry(frame_input, width=5)
input_rows.grid(row=1, column=1)
tk.Label(frame_input, text="Kolom:").grid(row=2, column=0)
input_cols = tk.Entry(frame_input, width=5)
input_cols.grid(row=2, column=1)

btn_buat = tk.Button(frame_input, text="Buat Matriks", command=buat_matriks)
btn_buat.grid(row=3, column=0, columnspan=2, pady=10)

# Frame untuk grid matriks
frame_matriks = tk.Frame(root)
frame_matriks.pack(pady=10)

# Tombol untuk menyelesaikan matriks
btn_selesaikan = tk.Button(root, text="Proses Eselon Baris", command=selesaikan)

# Output hasil
output = tk.Text(root, height=10, width=50)
output.pack(pady=10)

root.mainloop()
