myLinkedList = {
  'head':{
    'value':'one',
    'next':{
      'value':'two',
      'next':{
        'value':'three',
        'next':None
      }
    }
  }
}
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    '''
      Insert: We define a function that returns the node of the position index-1 because we want to remove the pointer to the next node and point it to  the new node.
      the next node will then be the currentNode.next.next, because currentNode.next is the pointer we want to point to the new Node, which we have next point to the nextNode

      Delete: works similarly, we get the currentnode(index-1) and point it to the currentNode.next.next, which will remove the reference to currentNode.next,hence gabbage collected
    '''
    def __init__(self,value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self,value):
        newNode = Node(value)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self #not very useful

    def prepend(self,value):
        newNode = Node(value) 
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self

    def printList(self):
      currentarray = self.head
      valuelist = []
      while currentarray:
          valuelist.append(currentarray.value)
          currentarray = currentarray.next
      return valuelist
          

    def insert(self,index,value):
        if type(index) is not int or index > self.length:
            raise KeyError("Invalid Index") 

        newNode = Node(value)
        currentNode = self.traverseToIndex(index) 
        if currentNode.next is  None:
            return self.append(value)
        newNode.prev = currentNode
        currentNode.next.prev = newNode
        newNode.next = currentNode.next
        currentNode.next = newNode
        self.length += 1
        return self

    def traverseToIndex(self, index):
        currentNode = self.head
        i=0
        while i != index-1:
            currentNode = currentNode.next
            i+=1
        return currentNode


    def remove(self,index):
        if type(index) is not int or index > self.length:
            raise KeyError("Invalid Index") 
        currentNode = self.traverseToIndex(index)   
        if currentNode.next is None or currentNode.next.next is None:    
            return
        nextNode = currentNode.next.next
        currentNode.next = nextNode
        self.length -= 1

    



print(0)      
ll1 = LinkedList(10)
print(ll1.head.prev)
print(1)   
ll1.append(5)
print(ll1.head.next.prev)
print(2)   
ll1.prepend(30)
print(ll1.head.next.next.prev)

print(3)   
ll1.insert(2,52)
print(ll1.printList())

print(4)   
ll1.remove(2)
print("delete", ll1.printList())

print(5)   
ll1.remove(2)
print("delete", ll1.printList())
