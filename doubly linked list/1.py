class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def addbr(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            return

    def addinbtw(self):
        data = int(input("Enter data : "))
        key = int(input("Enter key : "))
        now = self.head
        newnode = Node(data)
        while now.data != key:
            now = now.next
        if now.next is None:
            self.addnew(data)
            return
        newnode.next = now.next
        newnode.prev = now
        now.next = newnode
        newnode.next.prev = newnode
        self.show()

    def addnew(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = newnode
            newnode.prev = now

    def delbtw(self):
        key = int(input("Enter item to be deleted"))
        now = self.head
        while now.data != key:
            temp = now
            now = now.next
        temp.next = now.next
        if now.next is None:
            self.show()
            return
        now.next.prev = temp
        self.show()

    def dele(self):
        now = self.head
        while now.next:
            temp = now
            now = now.next
        temp.next = None
        self.show()
    def show(self):
        if not self.head:
            print("Empty list ")
        now = self.head
        while now:
            print(now.data, end=" ")
            now = now.next
        return print()

    def rev(self):
        now = self.head
        while now.next:
            now = now.next
        print()
        while now:
            print(now.data, end=" ")
            now = now.prev
        return


link = Linkedlist()
link.addbr(3)
link.addbr(2)
link.addbr(1)
link.addbr(0)
link.addnew(10)
link.addnew(20)
link.addnew(30)
link.addnew(40)
link.addnew(50)
link.addnew(60)
link.show()
# link.addinbtw()
# link.addinbtw()
# link.addinbtw()
print()
# link.rev()
print()
link.delbtw()
link.delbtw()
link.rev()
