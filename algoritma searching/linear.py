def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

data = [10, 20, 30, 40, 50]
cari = 30

hasil = linear_search(data, cari)
print("Ditemukan di indeks:", hasil)
