# Problem: 83
# Problem: LRU Cache
# Author: Kiranraj R.
# Date: 16/01/2026
# DSA topic: Design / Hash Map / Linked List
# Difficulty: Medium
# -------------------------------------------
# Time Complexity:  O(1) for get and put operations
# Space Complexity: O(capacity)
# -------------------------------------------
# Problem Statement:
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache
# Implement the LRUCache class:
# - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# - int get(int key) Return the value of the key if the key exists, otherwise return -1.
# - void put(int key, int value) Update the value of the key if the key
# exists. Otherwise, add the
# key-value pair to the cache. If the number of keys exceeds the capacity
# from this operation, evict
# the least recently used key.
# -------------------------------------------

# Approach:
# 1. Use an OrderedDict to maintain the order of usage.
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # To store key-value pairs

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end of the OrderedDict
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the key to the end
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove the first (least recently used) item
            self.cache.popitem(last=False)


# Example usage:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
print(cache.get(2))
