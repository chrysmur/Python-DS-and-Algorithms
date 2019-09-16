'''
>perfect binary tree - each node has 0 or two children
    - It is efficient
    - Number of total nodes doubles on each level
    -number of nodes in the last level= sum of all the nodes above it + 1. Half of the data is on the last level hence logN
    -Binary Search Tree O(logN) for insert, lookup and delete
        - Rules:
            > All values to the right of the main node must keep increasing
            >All values to the left must keep decreasing
    - Unbalanced search tree- it results in a linked list with O(n) operations for delete,lookup and insert

    BST - better than O(n), it is ordered, flexibility in size
        - Has no O(1)

       9
     4   20
    1 6 15 17
'''
class Node:
    '''binary tree'''
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.tree =None

    def insert(self,value):
        newNode = Node(value)
        if self.tree ==None:
            self.tree = newNode
            return self
        currentNode = self.tree
        while currentNode: 
            if newNode.value > currentNode.value:
                if not currentNode.right:
                    currentNode.right = newNode
                    return self
                currentNode = currentNode.right
            else:
                if not currentNode.left:
                    currentNode.left = newNode
                    return self
                currentNode = currentNode.left
            
    
    def lookup(self,value):        
        if self.tree.value == value:
            return "Found at Root"
        currentNode = self.tree
        while currentNode:
            if value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
            elif value == currentNode.value:
                return currentNode
        return False


bst = BST()


if __name__=="__main__":
    bst = BST()