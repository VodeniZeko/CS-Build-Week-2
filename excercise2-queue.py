# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        while self.q1:
            self.q2.append(self.q1.pop())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.pop())

    def pop(self):
        return self.q1.pop()

    def peek(self):
        return self.q1[-1]

    def empty(self):
        return not self.q1
