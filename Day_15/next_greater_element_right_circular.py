# Problem: 50
# Problem: Next Greater Element to the Right (Circular)
# Author: Kiranraj R.
# Data: 05/01/2026
# --------------------------------------------
# Given a circular integer array nums (meaning after the last element,
# it wraps back to the first), return an array ans where ans[i] is
# the next greater element of nums[i] The next greater element is the
# first element greater than nums[i] when moving right (wrapping around
# if needed) If no such element exists, ans[i] = -1

## For elements near the end, you’re allowed to continue searching from the start.
# Time Complexity: O(n)
# Space Complexity: O(n)


def next_greater_element_right_circular(arr):
    waiting_list = []
    n = len(arr)
    # Default should be -1 because if no next greater exists
    answer = [-1] * n

    # If you didn’t find a bigger number on the right in the first pass,
    # you get one more chance by looking from the start. For that we need our
    # range to be double.
    for i in range(n * 2):

        # To make sure once the last element is crossed, we wrap back to the start
        current_index = i % n
        # While current value is greater than the value stored at top
        # of stack, it becomes the "next greater" for that stacked element
        while waiting_list and arr[waiting_list[-1]] < arr[current_index]:
            old_index = waiting_list.pop()
            answer[old_index] = arr[current_index]

        # To avoid duplicates we should not insert items from the
        # second pass.
        if i < n:
            waiting_list.append(current_index)
    return answer


print(next_greater_element_right_circular([5, 4, 3, 2, 1]))
print(next_greater_element_right_circular([1, 2, 3, 4, 5]))
print(next_greater_element_right_circular([3, 2, 1]))
print(next_greater_element_right_circular([1, 2, 1]))
