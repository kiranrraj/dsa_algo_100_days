# Problem: 30
# Problem: Longest substring without repeating characters (Variable window sliding problem)
# Author: Kiranraj R.
# Date: 29/12/2025
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


# ## Longest Substring Without Repeating Characters

# Start with two pointers at the beginning of the string:
# left = start of current window
# right = end of current window (moves forward one step at a time)
# Use a dictionary (last_seen) to remember the last index where each character appeared.

# Move right across the string, one character at a time:

# Let ch be the character at position right.
# If we have seen this character and its last seen position is inside the current window (>= left):
# It means adding this character would create a duplicate inside the window.
# So, move left to one position after the previous occurrence of this character.
# This effectively removes the duplicate from the window.

# Update last_seen[ch] to the current index (right).

# This keeps track of the most recent occurrence of the character.

# Calculate the length of the current window:
# current_length = right - left + 1

# If this window is longer than the longest found so far, update:
# longest_length
# longest_substring

# Continue until right reaches the end of the string.

# Return the length and substring of the longest window that never had duplicate characters inside it.
