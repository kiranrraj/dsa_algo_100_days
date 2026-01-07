# Problem: 54
# Problem: Queue using two stacks
# Author: Kiranraj R.
# Data: 06/01/2026
# --------------------------------------------
# Time Complexity: O(1)
# Space Complexity: O(n)


class QueueUsingTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    # Add in_stack elements into out_stack if out_stack is empty.
    # This will ensure all the elements are accounted for
    def _shift_if_empty(self):
        # Only shift when out_stack is empty
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack

    def isEmpty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    # Make sure to check both stacks. out_stack last element will be
    # the top one. if in_stock is not empty add it into out_stock and
    # pop it.
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        elif self._shift_if_empty():
            return self.out_stack[-1]
        else:
            return self.out_stack[-1]

    # Always push into in_stack
    def enqueue(self, value):
        self.in_stack.append(value)

    # Dequeue must take lements from out_stack, if in_stack
    # is not empty add it to the out_stack and pop()
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        elif self._shift_if_empty():
            return self.out_stack.pop()
        else:
            return self.out_stack.pop()

    def display(self):
        if self.isEmpty():
            return "Queue is Empty"

        # front -> rear representation
        front_part = list(reversed(self.out_stack))  # front is out_stack[-1]
        rear_part = list(self.in_stack)

        res = ""
        for x in front_part + rear_part:
            res += str(x) + " <- "
        return res


q1 = QueueUsingTwoStacks()
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
