class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def kdist(root,dist):
    if(root is not None):
        if(dist == 0):
            print(root.data)
            return
        else:
            kdist(root.left, dist-1)
            kdist(root.right, dist-1)


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.right.left = Node('f')
root.right.right = Node('g')
root.left.left = Node('d')
root.left.right = Node('e')
root.left.left.left = Node('h')
root.left.left.right = Node('i')
root.right.left.right = Node('j')
root.right.right.left = Node('k')
root.right.right.right = Node('l')


kdist(root,3)
