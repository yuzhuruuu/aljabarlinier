#MENGUBAH MATRIKS MENJADI MATRIKS ESELON BARIS TEREDUKSI

import numpy as np
import tkinter as tk

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

        if matrix[r, lead] != 0 :
            matrix[r] = matrix[r] / matrix[r, lead]

        for i in range(nrows):
            if i != r:
                ratio = matrix[i, lead]
                matrix[i] = matrix[i] - ratio * matrix[r]

        lead += 1

    return matrix 
print("\nProgram Untuk Mengubah Matriks Menjadi Eselon Baris Tereduksi")
nrows = int(input("Masukan baris matriks: "))
ncols = int(input("Masukan kolom matriks: "))

print(f"\nMasukkan angka untuk setiap elemen matriks {nrows}x{ncols}: ")
matrix = np.zeros((nrows, ncols), dtype=float)

for i in range(nrows):
    for j in range(ncols):
        matrix[i][j] = float(input(f"Masukkan angka untuk elemen [{i + 1}][{j + 1}]: "))

print("\nMatriks yang dimasukkan:")
for row in matrix:
    print(" ", row)

result = row_echelon_form(matrix)

print("\nMatrix dalam bentuk eselon baris tereduksi")
for row in result:
    print(" ", row)