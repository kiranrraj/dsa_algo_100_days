# Problem: 25
# Problem: Move all zeros in array to the end
# Author: Kiranraj R.
# Date: 28/12/2025
# ----------------------------------------------------------------
def move_zeros(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    while pos < len(arr):
        arr[pos] = 0
        pos += 1
    return arr


print(move_zeros([1, 0, 2, 0, 3, 0, 4]))
