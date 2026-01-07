# Problem: 52
# Problem: Queue using stack
# Author: Kiranraj R.
# Data: 06/01/2026
# --------------------------------------------
# enqueue is O(1), but dequeue is O(n) due to pop(0).


class QueueUsingArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            res = ""
            for i in self.queue:
                res += str(i) + " <- "
            return res


q1 = QueueUsingArray()
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
