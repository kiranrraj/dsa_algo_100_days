# Problem: 29
# Problem: Check Anagram or not
# Author: Kiranraj R.
# Date: 29/12/2025
# ----------------------------------------------------------------
# Time Complexity:   O(n)
# Space Complexity:  O(1)


def get_string_dict(string):
    string_count = {}
    for i in string:
        string_count[i] = string_count.get(i, 0) + 1
    return string_count


def valid_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    return get_string_dict(string1) == get_string_dict(string2)


print(valid_anagram("kiran", "ran"))
print(valid_anagram("kiran", "krani"))
