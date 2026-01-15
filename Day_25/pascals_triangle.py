# Problem: 79
# Problem: Pascal's Triangle
# Author: Kiranraj R.
# Date: 15/01/2026
# DSA topic: Array
# Difficulty: Easy
# -------------------------------------------
# Time Complexity:  O(n^2)
# Space Complexity: O(n^2)
# -------------------------------------------
# Problem Statement:
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# -------------------------------------------
# Approach:
# 1. Initialize an empty list to hold the rows of Pascal's triangle.
# 2. Loop through the number of rows required.
# 3. For each row, initialize a list with 1s.
# 4. For each element in the row (except the first and last), calculate its
#    value as the sum of the two elements above it from the previous row.
# 5. Append the current row to the list of rows.
# 6. Return the list of rows.
# -------------------------------------------


def generate_pascals_triangle(numRows):
    triangle = []

    for row_num in range(numRows):
        # Start a new row with 1s
        row = [1] * (row_num + 1)

        # Each triangle element (except the first and last) is the sum of the two above it
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)

    return triangle
