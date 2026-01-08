# Problem: 55
# Problem: Queue using two stacks
# Author: Kiranraj R.
# Date: 06/01/2026
# --------------------------------------------
# Time Complexity: O(1)
# Space Complexity: O(n)


class QueueUsingTwoStacksOptimized:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _shift_if_empty(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def isEmpty(self):
        return not self.in_stack and not self.out_stack

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        self._shift_if_empty()
        if not self.out_stack:
            return "Queue is Empty"
        return self.out_stack[-1]

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        self._shift_if_empty()
        if not self.out_stack:
            return "Queue is Empty"
        return self.out_stack.pop()

    def display(self):
        res = ""
        self._shift_if_empty()
        for x in self.out_stack[::-1]:
            res += str(x) + " <- "
        return res


q1 = QueueUsingTwoStacksOptimized()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
print("Size of queue: ", q1.size())
print("Top of queue: ", q1.peek())
print("Elements of queue: ", q1.display())
print("Dequeue: ", q1.dequeue())
print("Elements of queue: ", q1.display())
print("Top of queue: ", q1.peek())
print("Size of queue: ", q1.size())
print("Dequeue: ", q1.dequeue())
print("Dequeue: ", q1.dequeue())
print("Elements of queue: ", q1.display())
print("Top of queue: ", q1.peek())
print("Size of queue: ", q1.size())
print(q1.dequeue())
print(q1.display())
print(q1.isEmpty())
print("Elements of queue: ", q1.display())
print("Top of queue: ", q1.peek())
print("Size of queue: ", q1.size())
