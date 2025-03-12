class Node:
    def __init__(self,data):
            self.data = data
            self.next = None
class Linkedlist:
    def __init__(self):
            self.head =None

        # delete from end
    def delend(self):
            if self.head is None:
                print("List is empty")
                return
            elif self.head.next is None:
                self.head = None

            else:
                now = self.head
                while now.next:
                    prev = now
                    now = now.next
                prev.next = None
                self.show()

        #delete from beginning
    def delfr(self):
            if self.head is None:
                print("List is empty")
                return
            else:
                now = self.head
                self.head = now.next
                self.show()
        #insert @ end
    def detany(self,data):
        prev = now = self.head
        self.show()
        if data == self.head.data:
            self.head = self.head.next
        while now.data != data :
            prev = now
            now = now.next
        prev.next = now.next


    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        self.show()
    def inst(self,data):
            if self.head is None:
                newnode = Node(data)
                self.head = newnode
                return
            else:
                newnode = Node(data)
                now = self.head
                newnode.next = now
                self.head = newnode
        #insert in between
    def inbtw(self,data,data1):
            newnode = Node(data)
            if self.head is None:
                self.head = newnode
                return
            else:
                now = self.head
                while now:
                    if now.data == data1:
                        newnode.next = now.next
                        now.next = newnode
                        return
                    now = now.next

        # insert @ beginning
    def ins(self,data):
            if self.head is None:
                newnode = Node(data)
                self.head = newnode
                return
            else:
                newnode = Node(data)
                now = self.head
                while now.next:
                    now = now.next
                now.next =newnode
                return

        #display the linked list
    def show(self):
            now = self.head

            while now:
                print(now.data, end='->')
                now = now.next
            print("Null")
            return


linkedlist = Linkedlist()
while True:
    print("1. insert @ end ")
    print("2. Display linked list")
    print("3. insert @ beginning ")
    print("4. Delete @ beginning")
    print("5. Delete from end ")
    print("6. insert in between")
    print("7. Reverse ")
    print("8. delete any node")
    print()
    choice = int(input("Enter the choice : "))
    if choice == 1:
        data = input("Enter the data ")
        linkedlist.ins(data)
        print()
    elif choice ==2:
        linkedlist.show()
        print()
    elif choice ==4:
        linkedlist.delfr()
        print()
    elif choice == 3:
        data = input("Enter the data ")
        linkedlist.inst(data)
        print()
    elif choice == 5:
        linkedlist.delend()
        print()
    elif choice ==6:
        data = input("Enter the data ")
        data1 = input("Enter the data ")
        linkedlist.inbtw(data,data1)

    elif choice == 7:
         linkedlist.reverse()
         print()
    elif choice ==8:
        data = input("Enter the data ")
        linkedlist.detany(data)
        print()
    else:
        break
linkedlist.ins(7)
linkedlist.ins(8)
linkedlist.ins(9)
linkedlist.ins(10)
linkedlist.ins(11)
linkedlist.ins(12)
linkedlist.detany(7)
linkedlist.detany(11)
linkedlist.detany(10)
linkedlist.detany(9)
linkedlist.detany(8)
linkedlist.show()



