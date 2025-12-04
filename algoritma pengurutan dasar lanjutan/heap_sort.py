# ===============================
#       HEAP SORT ALGORITHM
# ===============================

def heapify(arr, n, i):
    largest = i           # anggap root adalah yang terbesar
    left = 2 * i + 1      # anak kiri
    right = 2 * i + 2     # anak kanan

    # Jika anak kiri lebih besar dari root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Jika anak kanan lebih besar dari root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Jika root bukan yang terbesar, tukar
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Heapify ulang subtree yang terpengaruh
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Langkah 1: Bangun Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Langkah 2: Ekstrak elemen satu per satu
    for i in range(n - 1, 0, -1):
        # Pindahkan root (terbesar) ke posisi akhir
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify pada heap yang tersisa
        heapify(arr, i, 0)

    return arr


# ===============================
# Contoh Penggunaan
# ===============================

data = [12, 11, 13, 5, 6, 7]
print("Data sebelum diurutkan:", data)

sorted_data = heap_sort(data)
print("Data sesudah diurutkan:", sorted_data)
