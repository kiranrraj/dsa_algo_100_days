# Problem: 32
# Problem: Best Time to Buy and Sell Stock
# Author: Kiranraj R.
# Data: 30/12/2025
# --------------------------------------------
# Time complexity: O(n)
# Space complexity: O(1)


def best_buy(arr):
    buy = arr[0]
    max_profit = 0

    for price in arr:
        # if we find a lower price, update buy
        if price < buy:
            buy = price

        # check if selling today gives better profit
        profit = price - buy
        if profit > max_profit:
            max_profit = profit

    return max_profit


print(best_buy([10, 14, 3, 4, 5, 6]))
