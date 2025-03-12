class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertio(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        else:
            newnode.next = self.head
            self.head = newnode
            return

    def show(self):
        now = self.head
        while now:
            print(now.data,end=" -> ")
            now = now.next
        print("None")

link = Linkedlist()
li = [1,2,3,4,5,6,7]
for i in li:
    link.insertio(i)
link.show()