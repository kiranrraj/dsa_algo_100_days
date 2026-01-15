# Problem: 80
# Problem: Pascal's Triangle (Optimized)
# Author: Kiranraj R.
# Date: 15/01/2026
# DSA topic: Array
# Difficulty: Easy
# -------------------------------------------
# Time Complexity:  O(n^2)
# Space Complexity: O(n)
# -------------------------------------------
# Problem Statement:
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# -------------------------------------------
# Approach:
# 1. Initialize an empty list to hold the rows of Pascal's triangle.
# 2. Use a single list to build each row iteratively.
# 3. For each row, construct it using the previous row's values.
# 4. Append the current row to the list of rows.
# 5. Return the list of rows.
# -------------------------------------------


def generate_pascals_triangle(numRows):
    triangle = []
    row = []

    for i in range(numRows):
        if i == 0:
            row = [1]
        else:
            new_row = [1]
            for j in range(len(row) - 1):
                new_row.append(row[j] + row[j + 1])
            new_row.append(1)
            row = new_row

        triangle.append(row)

    return triangle


# Example usage:
numRows = 5
pascals_triangle = generate_pascals_triangle(numRows)
print(pascals_triangle)
# Output: [[1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
