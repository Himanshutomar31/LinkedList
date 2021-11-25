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
            print(str(temp.data)+" ",end="")
            temp = temp.next

    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            temp = temp.next
            count += 1
        return count


    def recLength(self):
        return self.recLengthHandler(self.head)


    def recLengthHandler(self, head):
        if head == None :
            return 0
        return 1 + self.recLengthHandler(head.next)



ll = LinkedList()
ll.insertAtFront(10)
ll.insertAtFront(20)
ll.insertAtEnd(30)
ll.insertAfter(50,2)
ll.printList()
print(ll.length())
print("rec" + str(ll.recLength()))





