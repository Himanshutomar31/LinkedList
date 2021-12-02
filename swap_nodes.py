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

    def remove_duplicate(self):
        hash = set()
        temp = self.head
        prev = None
        while temp != None:
            if temp.data in hash:
                prev.next = temp.next
                temp = temp.next
            else:
                hash.add(temp.data)
                prev = temp
                temp = temp.next

    def swap_nodes(self, x, y):
        prevX = None
        currX = self.head
        while currX != None:
            if currX.data == x:
                break
            else:
                prevX = currX
                currX = currX.next

        prevY = None
        currY = self.head
        while currY != None:
            if currY.data == y:
                break
            else:
                prevY = currY
                currY = currY.next

        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY

        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp


ll = LinkedList()
ll.insertAtEnd(40)
ll.insertAtEnd(90)
ll.insertAtEnd(20)
ll.insertAtEnd(50)
ll.printList()
print()
ll.swap_nodes(90,20)
ll.printList()





