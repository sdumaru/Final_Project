class AVLNode:
    def __init__(self, key, flight):
        self.key = key  # The flight number (used for sorting)
        self.flight = flight  # The flight object associated with this node
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Height of this node for balancing purposes

class AVLTree:
    def __init__(self):
        self.root = None

    # Helper function to get the height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Helper function to get the balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right rotate the subtree rooted with node y
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        # Return the new root
        return x

    # Left rotate the subtree rooted with node x
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        # Return the new root
        return y

    # Insert a flight into the AVL tree and return the new root of the subtree
    def insert(self, root, key, flight):
        # 1. Perform standard BST insert
        if not root:
            return AVLNode(key, flight)
        elif key < root.key:
            root.left = self.insert(root.left, key, flight)
        else:
            root.right = self.insert(root.right, key, flight)

        # 2. Update the height of the ancestor node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # 3. Get the balance factor to check if this node became unbalanced
        balance = self.get_balance(root)

        # 4. If the node is unbalanced, perform rotations

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Find the node with the smallest value (used for deletion)
    def find_min(self, root):
        if root is None or root.left is None:
            return root
        return self.find_min(root.left)

    # Delete a flight from the AVL tree
    def delete(self, root, key):
        # 1. Perform standard BST delete
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.find_min(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key
            root.flight = temp.flight

            # Delete the inorder successor
            root.right = self.delete(root.right, temp.key)

        # 2. If the tree has only one node, return it
        if not root:
            return root

        # 3. Update the height of the current node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # 4. Get the balance factor of this node
        balance = self.get_balance(root)

        # 5. If the node is unbalanced, perform rotations

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # In-order traversal of the AVL Tree (sorted flight numbers)
    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(f"Flight {root.flight.flight_number}: {root.flight.origin} -> {root.flight.destination}, Departure: {root.flight.departure_time}")
            self.in_order_traversal(root.right)