# ------------------------------------
# ARRAY / LIST 1 DIMENSI
# ------------------------------------
array_1d = [10, 20, 30, 40, 50]
print("Array 1 Dimensi:")
print(array_1d)
print("-------------------------")


# ------------------------------------
# ARRAY / LIST 2 DIMENSI
# (Array dalam array)
# ------------------------------------
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Array 2 Dimensi:")
for baris in array_2d:
    print(baris)
print("-------------------------")


# ------------------------------------
# ARRAY / LIST 3 DIMENSI
# (Array 2D di dalam array)
# ------------------------------------
array_3d = [
    [   # layer 1
        [1, 2],
        [3, 4]
    ],
    [   # layer 2
        [5, 6],
        [7, 8]
    ]
]

print("Array 3 Dimensi:")
for layer in array_3d:
    for baris in layer:
        print(baris)
    print("----- layer selesai -----")

