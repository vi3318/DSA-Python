# DFS traversal in a binary tree
# preorder, inorder, postorder


# Preorder traversal: root -> left -> right
def preorder(node):
    if node == None:
        return 
    print(node.val)
    preorder(node.left)
    preorder(node.right)

# TC O(N)
# SC O(H) where H is height of tree

# Inorder traversal: left -> root -> right
def inorder(node):
    if node == None:
        return 
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# Postorder traversal: left -> right -> root
def postorder(node):
    if node == None:
        return 
    postorder(node.left)
    postorder(node.right)
    print(node.val)