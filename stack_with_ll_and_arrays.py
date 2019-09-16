#creating a ll node 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
## Stack using linked lists
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = ''
        self.length = 0

    def peek(self):
        return self.top

    def push(self,val):
        #4-5-2-3
          newNode = Node(val)
          if self.length == 0:
              self.top = newNode
              self.bottom = newNode
          holdingPointer = self.top
          self.top = newNode
          self.top.next = holdingPointer
          self.length += 1

    def pop(self):
        if self.top.next is None:
            self.length -= 1
            return None

        if self.top ==self.bottom:
            self.bottom = None            

        holdingPointer = self.top.next
        self.top = holdingPointer
        self.length -= 1

class StackWithArrays:
    def __init__(self):
        self.stackArray = []
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if  len(self.stackArray) == 0:
            return None
        return self.stackArray[0]
    def push(self,val):
        self.stackArray.append(val)
        self.length += 1

        return self
    def pop(self):
        if self.length == 0:
            return
        self.length -= 1
        self.stackArray.pop()
        return self


st = StackWithArrays()
st.push("google")
st.push("udemy")
st.push("amazon")
print(st.stackArray)
print(st.pop())
print(st.pop())

print(st.length)