class Node:
    def __init__(self,data):
        self.left = None
        self.right= None
        self.key = data

    def insertion(self,data):
        if self.key is None:
            self.key =data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.left:
                self.left.insertion(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insertion(data)
            else:
                self.right = Node(data)

    def maxs(self):
        if self.right:
            self.right.maxs()
        else:
             print("maximum = ",self.key)

    def mins(self):
        if self.left:
            self.left.mins()
        else:
            print("minimum = ",self.key)
    def justprin(self):
        print("just here : ",self.key)
    def preorder(self):
        print(self.key,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def searching(self,data):
        if self.key == data:
            return print(data," is present")
        if data < self.key:
            if self.left:
                self.left.searching(data)
            else:
                return print(data," is absent")
        elif data > self.key:
            if self.right:
                self.right.searching(data)
            else:
                return print(data," is absent")

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key,end=" ")
        if self.right:
            self.right.inorder()

root = Node(None)
L1= [6,2,7,4,3,9]
for k in  L1:
    root.insertion(k)

root.preorder()
print()
root.inorder()
print()
root.searching(7)
print()
root.maxs()
root.mins()

