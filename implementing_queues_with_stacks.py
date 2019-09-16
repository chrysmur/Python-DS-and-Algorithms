#Creating Queue using Stack
#create a stack with lists
#create a queue

class Stack:
    def __init__(self):
        self.last = None
        self.first = None
        self.arrayStack  = []
        self.length = 0
    def push(self, value):
        self.arrayStack.append(value)
        self.last = self.arrayStack[0]
        self.first = value
        self.length += 1
    
    def pop(self):
        self.arrayStack.pop()
        self.length -= 1
        self.first = self.arrayStack[self.length-1]
        return self
    def peek(self):
        return self.last


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        self.queue = Stack()

    def enqueue(self, value):
        self.queue.push(value)
        self.first = self.queue.arrayStack[0]
        self.last = self.queue.arrayStack[-1]
        self.length = self.queue.length
        return self

    def dequeue(self):
        del self.queue.arrayStack[0]
        self.first = self.queue.arrayStack[0]
    
    def peek(self):
        return self.first


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
print(q.queue.arrayStack)