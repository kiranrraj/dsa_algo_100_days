# Problem: 97
# Problem: Coin Change Problem using Dynamic Programming
# Author: Kiranraj R.
# Date: 31/01/2026
# DSA Topic: Dynamic Programming
# Difficulty Level: Medium
# --------------------------------

# Problem Statement:
# You are given an integer array coins representing coins of different denominations
# and an integer amount representing a total amount of money. Return the fewest
# number of coins that you need to make up that amount. If that amount of money
# cannot be made up by any combination of the coins, return -1. You may assume
# that you have an infinite number of each kind of coin.
# --------------------------------

# Approach:
# 1. Create a dp array of size amount + 1 initialized to infinity.
# 2. Initialize dp[0] to 0 because zero coins are required to make amount 0.
# 3. Iterate through every amount from 1 to the target amount.
# 4. For each coin, check if it is smaller than or equal to the current amount.
# 5. If it is, update dp[amount] using the recurrence relation:
#    dp[amount] = min(dp[amount], 1 + dp[amount - coin])
# 6. If dp[amount] is still the initial 'infinity', return -1.
# 7. Otherwise, return dp[amount].
# --------------------------------

# Time Complexity:  O(n*m)
# Space Complexity: O(n)
# --------------------------------


def coin_change(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], 1 + dp[a - coin])

    return dp[amount] if dp[amount] != float("inf") else -1


# Example usage:
if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    result = coin_change(coins, amount)
    print(f"Input: coins = {coins}, amount = {amount}")
    print(f"Output: {result}")
    # Output: 3

    # Example 2:
    coins = [2]
    amount = 3
    result = coin_change(coins, amount)
    print(f"Input: coins = {coins}, amount = {amount}")
    print(f"Output: {result}")
    # Output: -1

    # Example 3:
    coins = [1]
    amount = 0
    result = coin_change(coins, amount)
    print(f"Input: coins = {coins}, amount = {amount}")
    print(f"Output: {result}")
    # Output: 0
