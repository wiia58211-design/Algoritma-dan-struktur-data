def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

data = [10, 20, 30, 40, 50]
cari = 40

hasil = binary_search(data, cari)
print("Ditemukan di indeks:", hasil)

