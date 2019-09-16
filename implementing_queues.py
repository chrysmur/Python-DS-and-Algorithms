class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        try:
            return self.first.value
        except:
            raise Exception("Empty Queue")

    def enqueue(self, value):
        newNode = Node(value)
        if self.first is None:
            self.first = self.last = newNode
        elif self.first == self.last:
            self.first.next = newNode
            self.last = newNode
        self.last.next = newNode
        self.last = newNode
        self.length += 1
        return self

    def dequeue(self):
        if self.first == self.last:
            self.first = self.last  = None
            return self
        self.first = self.first.next
        return self

            
newq = Queue()
newq.enqueue("harley")
newq.enqueue("tom")
newq.enqueue("mary")
newq.dequeue()
newq.dequeue()
newq.dequeue()

print(newq.first.value)
print(newq.last.value)