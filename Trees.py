class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Method to insert a new node in the tree
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)

    # Inorder traversal (Left, Root, Right)
    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder_traversal()
        return elements

    # Preorder traversal (Root, Left, Right)
    def preorder_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()
        return elements

    # Postorder traversal (Left, Right, Root)
    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()
        elements.append(self.data)
        return elements

    # Method to search for a node in the tree
    def search(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            return self.left.search(value)
        else:
            if self.right is None:
                return False
            return self.right.search(value)  # Fixed: Added missing closing parenthesis

# Example usage
if __name__ == "__main__":
    root = BinarySearchTree(10)
    root.insert(5)
    root.insert(20)
    root.insert(3)
    root.insert(7)
    root.insert(15)
    root.insert(25)

    print("Inorder Traversal:", root.inorder_traversal())  # Output: [3, 5, 7, 10, 15, 20, 25]
    print("Preorder Traversal:", root.preorder_traversal())  # Output: [10, 5, 3, 7, 20, 15, 25]
    print("Postorder Traversal:", root.postorder_traversal())  # Output: [3, 7, 5, 15, 25, 20, 10]
    print("Search 7:", root.search(7))  # Output: True
    print("Search 18:", root.search(18))  # Output: False
