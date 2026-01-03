# Problem: 43
# Problem: Reverse Method
# Author: Kiranraj R.
# Data: 02/01/2026
# --------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)


def reverseArray(arr, k):
    length = len(arr)
    # Reduces k so it’s always within 0 to length-1.
    k = k % length

    # reverse the part of the array from index start to end
    def reverse_section(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Reverse everything → fix the front → fix the back

    # Reverse the entire array.
    # Original:  [1, 2, 3, 4, 5, 6, 7]
    # Reversed:  [7, 6, 5, 4, 3, 2, 1]
    reverse_section(0, length - 1)
    # Reverse the first k elements.
    # Before: [7, 6, 5 | 4, 3, 2, 1]
    # After:  [5, 6, 7 | 4, 3, 2, 1]
    reverse_section(0, k - 1)
    # Reverse the remaining elements from index k to the end.
    # Before: [5, 6, 7 | 4, 3, 2, 1]
    # After:  [5, 6, 7 | 1, 2, 3, 4]
    reverse_section(k, length - 1)

    return arr


print(reverseArray([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
