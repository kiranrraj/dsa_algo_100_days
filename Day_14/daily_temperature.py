# Problem: 48
# Problem: Daily Temperatures
# Author: Kiranraj R.
# Data: 04/01/2026
# --------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# --------------------------------------------
# Given an integer array temperatures where temperatures[i] is the
# temperature on day i, return an array answer such that answer[i]
# is the number of days you must wait after day i to get a warmer
# temperature. If there is no future day for which this is possible,
# set answer[i] = 0.


def daily_temperatures(temperatures):
    n_of_temp = len(temperatures)

    # Answer array have same length as temperature array
    # each element will be 0.
    answer = [0] * n_of_temp

    # Array that hold temperatures that are waiting
    # format (temperature, index of the temperature)
    waiting = []

    for index, temp in enumerate(temperatures):

        # If current temp is warmer, we can resolve (answer) for
        # those waiting temps. Check if the stack have entry and
        # the top entry is less than current temperature. Means
        # the current temperature is warmer that the temperature
        # at the top of the stack.
        while waiting and waiting[-1][0] < temperatures[index]:

            # in that case we need to pop top elemet as we found warmer
            waiting_temp, waiting_index = waiting.pop()

            # now we need to update days we need to wait by index of
            # currennt temperature - index of lower temperature.
            answer[waiting_index] = index - waiting_index

        # if the temperature is lower, keep waiting by
        # adding to the waiting list as tuple(temp, index)
        # Even if temp is equal or lower than previous, it still waits.
        waiting.append((temp, index))

    return answer


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(daily_temperatures([30, 40, 50, 60]))
print(daily_temperatures([30, 60, 90]))
print(daily_temperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))
print(daily_temperatures([70, 70]))
