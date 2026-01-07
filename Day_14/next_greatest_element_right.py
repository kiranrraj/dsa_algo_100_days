# Problem: 49
# Problem: Next Greater Element to the Right
# Author: Kiranraj R.
# Data: 04/01/2026
# --------------------------------------------
# For each element, find the next element to its right that is greater. If none, -1.
# Time Complexity: O(n)
# Space Complexity: O(n)


def next_greater_element_right(arr):
    waiting_list = []
    # Default should be -1 because if no next greater exists
    answer = [-1] * len(arr)

    for i in range(len(arr)):
        # While current value is greater than the value stored at top
        # of stack, it becomes the "next greater" for that stacked element.
        while waiting_list and arr[waiting_list[-1]] < arr[i]:
            old_index = waiting_list.pop()
            answer[old_index] = arr[i]

        # Store (value, index) for elements still waiting for a greater element
        waiting_list.append(i)
    return answer


print(next_greater_element_right([5, 4, 3, 2, 1]))
print(next_greater_element_right([1, 2, 3, 4, 5]))
