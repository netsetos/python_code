class Node:
    def __init__(Node, data):
        Node.data = data
        Node.next = None

def reverse (head):   #reverse the Linked List
    if(head == None):
        return head
    curr = head
    prev=None
    while(curr!= None):
        nextNode=curr.next
        curr.next=prev
        prev=curr
        curr=nextNode
    return prev


def pallin(head):
    fast = head
    slow = head
    while fast is not None and fast.next is not None :
        fast = fast.next.next
        if fast is None:  # for even numbers
            mid = slow.next
            break

        if fast.next is None:   # for odd numbers
            mid=slow.next.next
            break
        slow = slow.next

    slow.next = None
    mid=reverse(mid)
    return head,mid

def compare(head,mid_reverse):                             #for comparing two Linked List
    while head is not None or mid_reverse is not None:
        if head.data != mid_reverse.data:
            return -1
        head = head.next
        mid_reverse = mid_reverse.next
    return 1



def printList(head):
    temp = head
    while (temp):
        print(temp.data)
        temp = temp.next


head = Node('R')
nodeB = Node('A')
nodeC = Node('D')

nodeD = Node('T')
nodeE = Node('A')
nodeF = Node('R')


head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF

a,r = pallin(head)
a=compare(a,r)
if(a==1):
    print("Pallindrome")
else:
    print("Not Pallindrome")


