# Problem: 58
# Problem: Minimum stack
# Author: Kiranraj R.
# Date: 08/01/2026
# --------------------------------------------
# Time Complexity
#   Operation	        Time
#   push	            O(1)
#   pop	                O(1)
#   get_min	            O(1)
#   peek	            O(1)
#   is_empty	        O(1)
#   size	            O(1)
# --------------------------------------------
# Space complexity: O(n)


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            pop_elem = self.stack.pop()
            if self.min_stack and self.min_stack[-1] == pop_elem:
                self.min_stack.pop()

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

    def is_empty(self):
        return not self.stack

    def size(self):
        return len(self.stack)

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None


s1 = MinStack()
s1.push(1)
s1.push(2)
s1.push(3)
print(s1.get_min())
