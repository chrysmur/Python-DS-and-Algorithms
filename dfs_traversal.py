import sys
sys.path.append('./')
from binarysearchtree import BST


def inorder_dfs(node,res):
    if node.left:
        inorder_dfs(node.left,res)
    res.append(node.value)
    if node.right:
        inorder_dfs(node.right,res)
    return res

def preorder_dfs(node,res):
    res.append(node.value)
    if node.left:
        preorder_dfs(node.left,res)
    if node.right:
        preorder_dfs(node.right,res)
    return res



def postorder_dfs(node, res):
    if node.left:
        postorder_dfs(node.left,res)
    if node.right:
        postorder_dfs(node.right,res)
    res.append(node.value)
    
    return res

if __name__ == "__main__":
    bst = BST()
    bst.insert(9)
    bst.insert(4)
    bst.insert(20)
    bst.insert(6)
    bst.insert(1)
    bst.insert(15)
    bst.insert(170)
    print(preorder_dfs(bst.tree,[]))
    print(inorder_dfs(bst.tree,[]))
    print(postorder_dfs(bst.tree,[]))