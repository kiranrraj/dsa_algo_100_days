# Problem: 32
# Problem: Best Time to Buy and Sell Stock
# Author: Kiranraj R.
# Date: 30/12/2025
# --------------------------------------------
# Time complexity: O(n)
# Space complexity: O(1)


def best_buy(arr):
    buy = float("inf")
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


# Same concept, different style
#
# def buy_sell(arr):
#     min_price = float("inf")
#     max_profit = 0
#     for price in arr:
#         min_price = min(min_price, price)
#         max_profit = max(max_profit, price - min_price)
#     return max_profit


# Brute Force Method
# Time complexity is O(n^2)
#
# def buy_sell(arr):
#     profit = 0
#     max_profit = 0
#     for i in range(len(arr)):
#         buy = arr[i]
#         for j in range(i+1, len(arr)):
#             profit = arr[j] - buy
#             max_profit = max(max_profit, profit)
#     return max_profit

# print(buy_sell([17,1,4,7,6]))
