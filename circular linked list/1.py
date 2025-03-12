class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def inse(self):
        data = int(input("Enter data : "))
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = newnode
        else:
            now = self.head
            while True:
                temp = now
                now = now.next
                if now == self.head:
                    break
            newnode.next = now
            temp.next = newnode

    def show(self):
        now = self.head
        while True:
            print(now.data,end= " ")
            now= now.next



link = Linkedlist()
link.inse()
link.inse()
link.inse()
link.inse()
link.show()