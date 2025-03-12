class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None

    def add(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = newnode
            return

    def show(self):
        now = self.head
        while(now):
            print(now.data,end=" ")
            now = now.next
        return

    def merge(self,other):
        now1 = self.head
        now2 = other.head
        dummy = Node(0)
        tail = dummy
        while now2 and now1:
            if now1.data < now2.data:
                tail.next = now1
                now1 = now1.next
            else:
                tail.next = now2
                now2 = now2.next
            tail = tail.next
            if now1:
                tail.next = now1
            if now2:
                tail.next = now2
        merlis = Linkedlist()
        merlis.head = dummy.next
        return merlis



linklist = Linkedlist()
linklist1 = Linkedlist()
linklist1.add(1)
linklist1.add(3)
linklist1.add(5)
linklist1.add(9)
linklist1.add(11)
linklist.add(2)
linklist.add(4)
linklist.add(6)
linklist.add(7)
linklist.add(8)
linklist.add(15)
linklist1.show()
print()
linklist.show()
print()
mergedlit = linklist1.merge(linklist)
print()
mergedlit.show()
