def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        # posisi berdasarkan rumus interpolasi
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1

data = [10, 20, 30, 40, 50]
cari = 50

hasil = interpolation_search(data, cari)
print("Ditemukan di indeks:", hasil)
