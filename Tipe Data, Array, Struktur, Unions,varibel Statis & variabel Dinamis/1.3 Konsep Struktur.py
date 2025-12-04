# Struktur menggunakan class
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

# Membuat objek dari struktur Mahasiswa
m1 = Mahasiswa("Andi", "20250123", "Teknik Informatika")

# Menampilkan data
print("Data Mahasiswa:")
print("Nama    :", m1.nama)
print("NIM     :", m1.nim)
print("Jurusan :", m1.jurusan)

