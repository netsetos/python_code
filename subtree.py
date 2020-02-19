class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isidentical(root1,root2):
    if(root1 == None and root2 == None):
        return True
    if(root1 != None and root2 != None and root1.data == root2.data):
        l = isidentical(root1.left , root2.left)
        r = isidentical(root1.right, root2.right)
        if(l and r):
            return True
        return False
    return  False

def issubtree(target,source):
    if(source is None):
        return True
    if(target is None):
        return False
    if isidentical(target,source):
        return True
    else:
        l=issubtree(target.left,source)
        r=issubtree(target.right, source)
        return l or r

target = Node('a')
target.left = Node('b')
target.right = Node('c')
target.right.left = Node('j')
target.right.right = Node('g')
target.left.left = Node('d')
target.left.right = Node('e')
target.left.left.left = Node('h')
target.left.left.right = Node('i')
target.left.right.right = Node('k')
target.right.right.right = Node('l')
target.right.right.left = Node('m')

source = Node('c')
source.left = Node('j')
source.right = Node('g')
# source.right.left = Node('z')
# source.right.right = Node('l')

if issubtree(target,source):
    print("Subtree")
else:
    print("Not a Subtree")