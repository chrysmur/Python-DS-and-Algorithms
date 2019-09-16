from  binaresearchtree import BST

def preorder_dfs(tree,res):
    print(tree.value)
    if tree.left:
        preorder_dfs(tree.left)


bst = BST()
preorder_dfs(bst.tree,[])