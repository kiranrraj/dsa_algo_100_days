# Problem: 33
# Problem: Highest product
# Author: Kiranraj R.
# Data: 31/12/2025
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(1)


def max_product_of_two(arr):
    if len(arr) < 2:
        return None

    largest = second_largest = float("-inf")
    smallest = second_smallest = float("inf")

    for n in arr:
        if n >= largest:
            second_largest = largest
            largest = n
        elif n > second_largest:
            second_largest = n

        if n <= smallest:
            second_smallest = smallest
            smallest = n
        elif n < second_smallest:
            second_smallest = n

    return max(largest * second_largest, smallest * second_smallest)


print(max_product_of_two([-5, 2, 3, 4, 0, -6]))
