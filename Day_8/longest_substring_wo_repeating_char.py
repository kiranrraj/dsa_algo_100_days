# Problem: 30
# Problem: Longest substring without repeating characters (Variable window sliding problem)
# Author: Kiranraj R.
# Data: 29/12/2025
# --------------------------------------------
# Time complexity: O(n)
# Space complexity: O(n)


def longest_non_repeating_subarray(string):

    left = 0
    longest = 0
    subarray = ""
    last_seen = {}

    for right, ch in enumerate(string):

        # if the char is seen and the char index is greater than the left index of
        # our window that means the char is inside our window (current subarray)
        if ch in last_seen and last_seen[ch] >= left:

            # move the start to right of the character
            left = last_seen[ch] + 1

        # updating current chars's last seen position
        last_seen[ch] = right

        # get current window
        current_len = right - left + 1

        # if current window is the longest set it as longest
        if current_len > longest:
            longest = current_len
            subarray = string[left : right + 1]

        # or if no need to return the sub array
        # longest = max(longest, current_len)

    return longest, subarray


print(longest_non_repeating_subarray("helo"))
print(longest_non_repeating_subarray("hello"))
