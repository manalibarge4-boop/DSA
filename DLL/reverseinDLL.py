
class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def print(self):
        temp = self.head
        print("List elements:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def print_reverse(self):
        temp = self.head

        if temp is None:
            return

        while temp.next:
            temp = temp.next

        print("Reverse order:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.prev

        print()


list1 = LinkedList()

list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))
list1.append(Node(78))

list1.print()
list1.print_reverse()
