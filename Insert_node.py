class Node:
    def __init__(Node, data):
        Node.data = data
        Node.next = None


def insertNode(head, newNode):
    newNode.next = head
    head = newNode
    return head


def insertmiddle(head, newNode):
    curr = head
    while (curr.data != 'e'):
        curr = curr.next
    newNode.next = curr.next
    curr.next = newNode
    return head


def insertend(head, newNode):
    curr = head
    while (curr.next != None):
        curr = curr.next
    curr.next = newNode
    newNode.next = None
    return head







def printList(head):
    temp = head
    while (temp):
        print(temp.data)
        temp = temp.next


head = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF

# head=insertNode(head,Node('z'))
# head=insertmiddle(head,Node('z'))
head = insertend(head, Node('z'))
printList(head)
