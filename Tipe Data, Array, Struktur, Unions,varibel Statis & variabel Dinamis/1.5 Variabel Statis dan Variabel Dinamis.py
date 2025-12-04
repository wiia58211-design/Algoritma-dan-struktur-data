class Mahasiswa:
    # Variabel statis
    universitas = "Universitas Teknologi Indonesia"

    def __init__(self, nama, nim):
        # Variabel dinamis dibuat di sini (per objek)
        self.nama = nama
        self.nim = nim

# Objek pertama
m1 = Mahasiswa("Andi", "20250123")

# Objek kedua
m2 = Mahasiswa("Budi", "20250145")

print("Variabel Statis:")
print(m1.universitas)
print

