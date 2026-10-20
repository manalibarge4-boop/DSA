# Concatenate two SLL


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self) :
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

    def concatenate(self):
       temp=self.head
       if temp == None:
            self.head = list2.head
            return
       while(temp.next):
          temp = temp.next
       temp.next = list2.head          

    def print(self):
       print("List elements: ") 
       temp = self.head
       while temp:
          print(temp.val, end=" ")  #can use data
          temp = temp.next
       print()        
         
       

#SLL = SinglyLinkedList()
#SLL.traversal()  o/p SLL is empty

SLL = SinglyLinkedList()
SLL.append(10)
SLL.append(20)
SLL.append(30)

list2 = SinglyLinkedList()
list2.append(40)
list2.append(50)
list2.append(60)


print("First SLL:")
SLL.traversal()

print("Second SLL:")
list2.traversal()

SLL.concatenate()

print("After concatenation:")
SLL.print()