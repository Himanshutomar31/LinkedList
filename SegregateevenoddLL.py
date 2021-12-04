from reverseLL import Node, LinkedList


def segregarte_even_odd(ll):
    temp = ll.head
    evenHead = None
    evenCurr = None
    oddHead = None
    oddCurr = None
    while temp != None:
        if temp.data%2 == 0:
            if evenHead == None:
                evenHead = temp
                evenCurr = temp
            else:
                evenCurr.next = temp
                evenCurr = temp
        else:
            if oddHead == None:
                oddHead = temp
                oddCurr = temp
            else:
                oddCurr.next = temp
                oddCurr = temp

        temp = temp.next

    evenCurr.next = oddHead
    ll.head = evenHead



ll = LinkedList()
ll.insertAtFront(1)
ll.insertAtFront(8)
ll.insertAtFront(12)
ll.insertAtFront(3)
ll.insertAtFront(2)
ll.insertAtFront(5)
ll.printList()
print()
segregarte_even_odd(ll)
ll.printList()
