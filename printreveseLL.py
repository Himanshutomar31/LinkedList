from reverseLL import Node, LinkedList



def print_reverseLL(head):
    if head == None:
        return
    print_reverseLL(head.next)
    print(head.data, end=" ")



ll = LinkedList()
ll.insertAtFront(1)
ll.insertAtFront(8)
ll.insertAtFront(12)
ll.insertAtFront(3)
ll.insertAtFront(2)
ll.insertAtFront(5)
ll.printList()
print()
print_reverseLL(ll.head)

