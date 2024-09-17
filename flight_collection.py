# Simple AVL Tree Implementation code obtained from GeeksforGeeks
# Need to make more changes based on Flight information

class AVLNode:
    def __init__(self, flight):
        self.flight = flight
        self.height = 1  # Height of this node
        self.left = None  # Left child
        self.right = None  # Right child

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    # Insert a new flight into the AVL tree
    def insert(self, root, flight):

        # Perform normal BST insert
        if not root:
            return AVLNode(flight)
        elif flight < root.flight:
            root.left = self.insert(root.left, flight)
        else:
            root.right = self.insert(root.right, flight)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Balance the tree if it's unbalanced
        # Left rotation
        if balance > 1 and flight < root.left.flight:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and flight > root.right.flight:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and flight > root.left.flight:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and flight < root.right.flight:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # In-order traversal to display flights in sorted order based on some criteria
    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        flight = node.flight
        print(f"Flight {flight}")
        self.in_order(node.right)
