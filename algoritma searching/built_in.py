# =========================================
# BUILT-IN SEARCHING PYTHON
# =========================================

data = [10, 20, 30, 40, 50]

print("Data:", data)

# 1. Pencarian menggunakan 'in'
print("\n1. Menggunakan 'in'")
print(30 in data)   # True
print(100 in data)  # False

# 2. Pencarian menggunakan 'not in'
print("\n2. Menggunakan 'not in'")
print(60 not in data)  # True
print(20 not in data)  # False

# 3. Menggunakan index()
print("\n3. Menggunakan index()")
try:
    idx = data.index(40)
    print("Index dari 40:", idx)
except ValueError:
    print("Data tidak ditemukan")

# 4. Menggunakan count()
print("\n4. Menggunakan count()")
print("Jumlah kemunculan angka 20:", data.count(20))
print("Jumlah kemunculan angka 70:", data.count(70))

# 5. Mencari nilai maksimum dan minimum
print("\n5. Menggunakan max() dan min()")
print("Nilai terbesar:", max(data))
print("Nilai terkecil:", min(data))

# 6. any() dan all()
print("\n6. Menggunakan any() dan all()")
print("Apakah ada angka > 40?:", any(x > 40 for x in data))
print("Apakah semua angka > 5?:", all(x > 5 for x in data))
print("Apakah semua angka < 40?:", all(x < 40 for x in data))
