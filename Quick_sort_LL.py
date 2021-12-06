from reverseLL import Node, LinkedList


def partition(head):
    temp = head.next
    ref = temp
    prevRef = None
    pivot = head
    count = 0
    while temp != None:
         if temp.data < pivot.data:
             count += 1
             temp2 = temp.data
             temp.data = ref.data
             ref.data = temp2
             prevRef = ref
             ref = ref.next
         temp = temp.next
    if prevRef is not None:
        temp2 = prevRef.data
    else:
        return pivot
    prevRef.data = pivot.data
    pivot.data = temp2
    return prevRef



def Quick_sortLLHandler(head):
    if head == None or head.next == None:
        return head
    pNode = partition(head)
    temp = pNode.next
    pNode.next = None
    Quick_sortLLHandler(head)
    Quick_sortLLHandler(temp)
    pNode.next = temp
    return head



def Quick_sortLL(ll):
    ll.head = Quick_sortLLHandler(ll.head)


ll = LinkedList()
ll.insertAtFront(1)
ll.insertAtFront(9)
ll.insertAtFront(3)
ll.insertAtFront(2)
ll.insertAtFront(19)
ll.insertAtFront(13)
ll.insertAtFront(12)
ll.printList()
print()
Quick_sortLL(ll)
ll.printList()

