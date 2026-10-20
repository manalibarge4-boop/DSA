#Delete alternate node in SLL

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

    def del_alternate(self):
        prev = self.head
        temp = self.head.next

        while prev and temp:
            prev.next = temp.next
            temp = None
            prev = prev.next

            if prev:
                temp = prev.next


SLL = SinglyLinkedList()
SLL.append(10)
SLL.append(20)
SLL.append(30)
SLL.append(40)
SLL.append(1)

print("Before deleting alternate nodes:")
SLL.traversal()

SLL.del_alternate()

print("After deleting alternate nodes:")
SLL.traversal()
