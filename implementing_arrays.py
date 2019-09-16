##Creating lists Manually 

class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[len(self.data)] = item
        self.length += 1

    def pop(self):
        del self.data[len(self.data)-1]
        self.length -= 1

    def delete(self,index):
        del self.data[index]
        self.shiftItems(index)
    
    def shiftItems(self,index):
        for i in range(index, self.length-1):
            self.data[i]=self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1




newarray = Array()
newarray.push(1)
newarray.push(2)
newarray.push(3)
newarray.push(4)
newarray.push(5)
print(newarray.length)
newarray.delete(2)
print(newarray.length)
    