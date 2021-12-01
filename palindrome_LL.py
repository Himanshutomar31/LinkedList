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

    def reverseIteration(self):
        temp = self.head
        prev = None
        next = temp
        while temp != None:
            next = temp.next
            if next is None:
                self.head = temp
                temp.next = prev
                temp = None
            else:
                temp.next = prev
                prev = temp
                temp = next


    def is_palindrome(self):
        temp = self.head
        s1 = ''
        while temp != None:
            s1 = s1 + str(temp.data)
            temp = temp.next

        self.reverseIteration()
        temp = self.head
        s2 = ''
        while temp != None:
            s2 = s2 + str(temp.data)
            temp = temp.next
        if s1 == s2 :
            return  True
        return  False

    def is_palindrome1(self):
        return self.is_palindrome1_Handler(self.head)

    def is_palindrome1_Handler(self, right):
        global left
        left = self.head

        if right == None:
            return True

        check = self.is_palindrome1_Handler(right.next)
        if check == False:
            return False

        if right.data == left.data:
            left = left.next
            return True

        return False


ll = LinkedList()
ll.insertAtEnd(30)
ll.insertAtEnd(40)
ll.insertAtEnd(90)
ll.insertAtEnd(40)
ll.insertAtEnd(30)
#print(ll.is_palindrome())
print(ll.is_palindrome1())
ll.printList()





