
# Find the middle node and delete it

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node

    def traversal(self):
        if self.head == None:
            print("SLL is empty")
        else:
            curr = self.head
            while curr != None:
                print(curr.val, end=" ")
                curr = curr.next
            print()

    def findmid_del(self):
        temp = temp1 = self.head
        prev = None

        if self.head == None:
            print("SLL is empty")
            return

        while temp1 and temp1.next:
            prev = temp
            temp = temp.next
            temp1 = temp1.next.next

        print("Middle Node:", temp.val)

        if prev == None:
            self.head = temp.next
        else:
            prev.next = temp.next

        temp = None


SLL = SinglyLinkedList()
SLL.append(10)
SLL.append(20)
SLL.append(30)
SLL.append(40)
SLL.append(1)

SLL.traversal()
SLL.findmid_del()
SLL.traversal()
