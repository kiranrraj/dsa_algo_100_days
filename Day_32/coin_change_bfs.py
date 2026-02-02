# Problem: 98
# Problem: Coin Change Problem (Breath-First Search Approach)
# Author: Kiranraj R.
# Date: 31/01/2026
# DSA Topic: Graphs - BFS
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
# 1. Use a queue to perform BFS, starting from amount 0.
# 2. For each coin, check if it is smaller than or equal to the current amount.
# 3. If it is, add the new amount (current amount + coin) to the queue.
# 4. Keep track of the number of coins used to reach each amount.
# 5. If we reach the target amount, return the number of coins used.
# 6. If we reach the end of the queue without finding the target amount, return -1.
# --------------------------------

# Time Complexity: O(n*m)
# Space Complexity: O(n)
# -----------------

from collections import deque


def coin_change(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    queue = deque([(0, 0)])  # (current_total, num_coins)
    visited = {0}

    while queue:
        current_sum, steps = queue.popleft()

        for coin in coins:
            next_sum = current_sum + coin

            if next_sum == amount:
                return steps + 1

            if next_sum < amount and next_sum not in visited:
                visited.add(next_sum)
                queue.append((next_sum, steps + 1))

    return -1


# Example usage:
if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    result = coin_change(coins, amount)
    print(f"Input: coins = {coins}, amount = {amount}")
    print(f"Output: {result}")

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
