from binarysearchtree import BST
bst = BST()
bst.insert(9)
bst.insert(4)
bst.insert(20)
bst.insert(170)
bst.insert(1)
bst.insert(6)
bst.insert(15)


def traverse_bfs(tree):
    '''iterative appraoch'''
    currentNode = bst.tree
    queue = [currentNode]
    result = []
    while queue:
        currentNode = queue.pop(0)
        result.append(currentNode.value)
        
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

    return result

def traverse_bfs_r(queue, result):
    '''recursive'''
    if not queue:
        return result
    currentNode = queue.pop(0)
    result.append(currentNode.value)
    if currentNode.left:
        queue.append(currentNode.left)
    if currentNode.right:
        queue.append(currentNode.right)
    return traverse_bfs_r(queue, result)
    
print(traverse_bfs_r([bst.tree],[]))