class Node:
    def __init__(self,data):
        self.right = None
        self.key = data
        self.left = None

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

    def preorder(self):
        print(self.key,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key,end=" ")
    def inorder(self):

        if self.left:
            self.left.inorder()
        print(self.key,end=" ")
        if self.right:
            self.right.inorder()


    def serching(self,data):
        if self.key is None:
            return print("Tree is Empty")
        if self.key == data:
            return print( "Element Found ")
        if self.key > data:
            if self.left:
                self.left.serching(data)
            else:
                return print( "Element not found")
        else:
            if self.right:
                self.right.serching(data)
            else:
                return print("Element not found")

    def deletion(self, data):
        if self.key is None:
            print("Tree is empty!")
            return None
        # Traverse to the left subtree
        if data < self.key:
            if self.left:
                self.left = self.left.deletion(data)
            else:
                print("Given node is not present in the Tree!")
        # Traverse to the right subtree
        elif data > self.key:
            if self.right:
                self.right = self.right.deletion(data)
            else:
                print("Given node is not present in the Tree!")
        # Node to be deleted found
        else:
            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            # Node with two children: Get the in-order successor
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.deletion(node.key)  # Correct key passed
        return self


root = Node(None)
li = [5,4,9,8,10,2,3]
for k in li:
    root.insertion(k)
root.serching(3)
print()
print("pre order")
root.preorder()
print()
print("in order")
root.inorder()
print()
print("post order")
root.postorder()
print()
print()
root.preorder()
print()
root.deletion(5)
root.deletion(2)
root.preorder()
print()
