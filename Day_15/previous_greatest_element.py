# Problem: 50
# Problem: Previous Greater Element (to the Left)
# Author: Kiranraj R.
# Data: 05/01/2026
# --------------------------------------------
# For each element, find the nearest greater element on its left. If none, -1.

## As you move from left to right, remove all smaller numbers on the left, and the
# first bigger number you see on the left is the answer. if none exists, return -1.

# Time Complexity: O(n)
# Space Complexity: O(n)


def previous_greater_element(arr):
    waiting_list = []
    answer = [-1] * len(arr)

    for i in range(len(arr)):
        # Pop all elements that are <= current element because:
        # they cannot be previous greater for current and they also
        # cannot help future elements that are >= current
        while waiting_list and arr[waiting_list[-1]] <= arr[i]:
            waiting_list.pop()

        # After popping, if stack is empty => no greater element
        # on the left else stack top is the nearest greater on the left
        if waiting_list:
            answer[i] = arr[waiting_list[-1]]

        # Push current index
        waiting_list.append(i)

    return answer


print(previous_greater_element([4, 20, 17, 28, 14, 9]))
print(previous_greater_element([10, 4, 2, 20, 40, 12, 30]))
