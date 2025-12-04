def shell_sort(arr):
    n = arr.size
    # Gap awal = setengah panjang array
    gap = n // 2

    # Selama gap masih > 0
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Geser elemen hingga posisi yang benar ditemukan
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        # Gap diperkecil
        gap //= 2


# Contoh penggunaan
import numpy as np

data = np.array([23, 12, 1, 8, 34, 54, 2, 3])
print("Sebelum sorting:", data)

shell_sort(data)
print("Sesudah sorting:", data)
