""" Balanced binary search tree to maintain flight records and help in sorting """

from flights import Flight

class AVLNode:
    """ Individual flight node which will be inserted in the tree """
    def __init__(self, key, flight):
        self.key = key                      # The key used for sorting (can be flight_id, price, departure_time)
        self.flight = flight                # The flight object associated with this node
        self.left = None                    # Left child
        self.right = None                   # Right child
        self.height = 1                     # Height of this node for balancing purposes

class FlightAVLTree:
    """ Collection of flights that will be used for sorting """
    def __init__(self):
        self.root = None

    def get_height(self, node):
        """ Helper function to get the height of a node """
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """ Helper function to get the balance factor of a node """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        """ Right rotate the subtree rooted with node y """
        x = y.left
        temp = x.right

        # Perform rotation
        x.right = y
        y.left = temp

        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        # Return the new root
        return x

    def left_rotate(self, x):
        """ Left rotate the subtree rooted with node x """
        y = x.right
        temp = y.left

        # Perform rotation
        y.left = x
        x.right = temp

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        # Return the new root
        return y

    def insert(self, root, key, flight):
        """ Insert a flight into the AVL tree and return the new root of the subtree """
        # Perform standard BST insert
        if not root:
            return AVLNode(key, flight)
        elif key < root.key:
            root.left = self.insert(root.left, key, flight)
        else:
            root.right = self.insert(root.right, key, flight)

        # Update the height of the ancestor node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Get the balance factor to check if this node became unbalanced
        balance = self.get_balance(root)

        # If the node is unbalanced, perform rotations
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

    def find_min(self, root):
        """ Find the node with the smallest value (used for deletion) """
        if root is None or root.left is None:
            return root
        return self.find_min(root.left)

    def delete(self, root, key):
        """ Delete a flight from the AVL tree """
        # Perform standard BST delete
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

        # If the tree has only one node, return it
        if not root:
            return root

        # Update the height of the current node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Get the balance factor of this node
        balance = self.get_balance(root)

        # If the node is unbalanced, perform rotations

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

    def in_order_traversal(self, root):
        """ In-order traversal of the AVL Tree (sorted flight based on key) """
        if root:
            self.in_order_traversal(root.left)
            print(f"Flight {root.flight.flight_no}: {root.flight.origin} -> {root.flight.destination}, Departure: {root.flight.departure_time}, Price: {root.flight.price}")
            self.in_order_traversal(root.right)

# Example Usage
flight_tree = FlightAVLTree()

# Create flights with flight number, departure time, origin, destination, price, and seat_number
flights_list = [
    Flight(123, "08:00", "New York", "Dallas", 600, 20),
    Flight(456, "09:30", "Los Angeles", "New York", 1000, 16),
    Flight(789, "11:15", "Chicago", "Las Vegas", 300, 30),
    Flight(101, "12:45", "Miami", "San Diago", 450, 20),
    Flight(654, "14:30", "Houston", "Boston", 650, 10),
    Flight(321, "17:00", "San Francisco", "Chicago", 300, 15)
]

# Insert flights into the AVL tree
for fli in flights_list:
    flight_tree.root = flight_tree.insert(flight_tree.root, fli.departure_time, fli)

# Show the flights in sorted order by flight number
print("Flights in Sorted Order by Flight Number:")
flight_tree.in_order_traversal(flight_tree.root)
