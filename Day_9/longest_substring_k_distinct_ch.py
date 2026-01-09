# Problem: 31
# Problem: Longest substring with at most K distinct characters
# Author: Kiranraj R.
# Date: 30/12/2025
# --------------------------------------------
# Time complexity: O(n)
# Space complexity: O(n)


def longest_subarray_with_k_distinct_chars(string, k):
    left = 0
    longest = 0
    subarray = ""
    char_dict = {}

    # Increment the char frequecy by 1
    for right, ch in enumerate(string):
        char_dict[ch] = char_dict.get(ch, 0) + 1

        # If decreasing the count doesn’t reach 0, the character is still in
        # the window, so we keep shrinking until some character fully leaves,
        # bringing the distinct count back down to k.
        while len(char_dict) > k:
            left_char = string[left]
            # reduce the frequency of the leftmost character
            char_dict[left_char] -= 1
            # if leftmost character is zero, delete that
            if char_dict[left_char] == 0:
                del char_dict[left_char]
            # move the left by 1
            left += 1

        # Current longest
        current_len = right - left + 1
        if current_len > longest:
            longest = current_len
            subarray = string[left : right + 1]

    return longest, subarray
