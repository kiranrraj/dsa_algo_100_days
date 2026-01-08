# Problem: 53
# Problem: Queue using deque
# Author: Kiranraj R.
# Date: 06/01/2026
# --------------------------------------------
# # O(1) enqueue (append) and O(1) dequeue (popleft).

from collections import deque


class QueueUsingDeque:
    def __init__(self):
        self.queue = deque()

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queue[0]

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.popleft()

    def display(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            res = ""
            for i in self.queue:
                res += str(i) + " <- "
            return res


q1 = QueueUsingDeque()
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
