class Node:
    def __init__(Node, data):
        Node.data = data
        Node.next = None
        Node.prev = None


def insertNodestart(head, newNode):
    newNode.next = head
    head.prev = newNode
    newNode.prev=None
    head=newNode
    return head


def insertmiddle(head, newNode):
    temp = head
    while (temp.data != 'c'):
        temp = temp.next
    buffer = temp.next
    temp.next = newNode
    newNode.prev = temp
    newNode.next = buffer
    buffer.prev = newNode
    return head


def insertend(head, newNode):
    temp = head
    while (temp.next != None):
        temp = temp.next
    temp.next = newNode
    newNode.prev = temp
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



head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD



nodeB.prev=head
nodeC.prev=nodeB
nodeD.prev=nodeC



# head=insertNodestart(head,Node('z'))
# head=insertmiddle(head,Node('z'))
head = insertend(head, Node('z'))
printList(head)

