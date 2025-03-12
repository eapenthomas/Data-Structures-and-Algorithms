class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head =None

    def reverse(self):
        now = self.head
        prev = None
        while now:
            temp = now.next
            now.next= prev
            prev =now
            now = temp
        self.head = prev
    def insertion(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            newnode = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
            return

    def show(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current= current.next
        print("None")

linklist = Linkedlist()
linklist.insertion(4)
linklist.insertion(5)
linklist.insertion(6)
linklist.show()
linklist.reverse()
linklist.show()