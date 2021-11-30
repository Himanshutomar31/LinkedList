class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    #insert Node at the front
    def insertAtFront(self, data):
        new_node = Node(data)
        self.len += 1
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    #Insert node at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        self.len += 1
        if self.head is None:
            self.head = new_node
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = new_node

    # insert after a node
    def insertAfter(self, data, num):
        if num > self.len :
            return
        new_node = Node(data)
        self.len += 1
        count = 1
        temp = self.head
        while count < num:
            temp = temp.next
            count +=1

        new_node.next = temp.next
        temp.next = new_node

    # print List

    def printList(self):
        temp = self.head
        while temp != None:
            print(str(temp.data)+" ", end="")
            temp = temp.next

    #find middle
    def findMiddle(self):
        slow = self.head
        fast = self.head
        while fast.next != None and fast.next.next != None :
            slow = slow.next
            fast = fast.next.next
        return slow

    def find_loop(self):
        s = set()
        temp = self.head
        while temp != None:
            if temp in s:
                return True
            else:
                s.add(temp)
                temp = temp.next
        return False

    # find loop way 2
    def find_loop2(self):
        slow = self.head
        fast = self.head
        while fast != None and slow != None and fast.next != None :
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


ll = LinkedList()
ll.insertAtFront(10)
ll.insertAtFront(20)
ll.insertAtFront(60)
ll.insertAtFront(70)
n = Node(60)
ll.head.next.next.next = n
n.next = ll.head
print(ll.find_loop())
print(ll.find_loop2())
#ll.printList()





