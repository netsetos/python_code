class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def get_mirror(root):
    if(root == None):
        return
    get_mirror(root.left)
    get_mirror(root.right)

    temp=root.left
    root.left=root.right
    root.right=temp

def preorder(root):
    if(root==None):
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)
