""" Balanced binary search tree to maintain flight records and help in sorting """

import random
import time
from flights import Flight

class AVLNode:
    """ Individual flight node which will be inserted in the AVL tree """
    def __init__(self, key, flight):
        self.key = key                      # Key used for sorting (e.g., flight_id, price, departure_time)
        self.flight = flight                # Flight object associated with this node
        self.left = None                    # Left child
        self.right = None                   # Right child
        self.height = 1                     # Height of this node for balancing purposes
        self.size = 1                       # Size of the subtree rooted at this node

class FlightAVLTree:
    """ Collection of flights that will be used for sorting and retrieval """
    def __init__(self, rebalance_threshold=2):
        self.root = None
        self.rebalance_threshold = rebalance_threshold  # Set a threshold for lazy rebalancing

    def get_height(self, node):
        """ Helper function to get the height of a node """
        return 0 if not node else node.height

    def get_size(self, node):
        """ Helper function to get the size of a subtree rooted at the node """
        return 0 if not node else node.size

    def update_node_attributes(self, node):
        """ Updates the height and size attributes of the node """
        if node:
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            node.size = self.get_size(node.left) + self.get_size(node.right) + 1

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

        # Update heights and sizes
        self.update_node_attributes(y)
        self.update_node_attributes(x)

        # Return the new root
        return x

    def left_rotate(self, x):
        """ Left rotate the subtree rooted with node x """
        y = x.right
        temp = y.left

        # Perform rotation
        y.left = x
        x.right = temp

        # Update heights and sizes
        self.update_node_attributes(x)
        self.update_node_attributes(y)

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

        # Update the node's attributes (height and size)
        self.update_node_attributes(root)

        # Get the balance factor to check if this node became unbalanced
        balance = self.get_balance(root)

        # If the node is unbalanced and the imbalance exceeds the lazy threshold, perform rotations
        if balance > self.rebalance_threshold and key < root.left.key:          # Left Left Case
            return self.right_rotate(root)
        if balance < -self.rebalance_threshold and key > root.right.key:        # Right Right Case
            return self.left_rotate(root)
        if balance > self.rebalance_threshold and key > root.left.key:          # Left Right Case
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -self.rebalance_threshold and key < root.right.key:        # Right Left Case
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

        # Update the node's attributes (height and size)
        self.update_node_attributes(root)

        # Get the balance factor of this node
        balance = self.get_balance(root)

        # If the node is unbalanced and the imbalance exceeds the lazy threshold, perform rotations

        # Left Left Case
        if balance > self.rebalance_threshold and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > self.rebalance_threshold and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -self.rebalance_threshold and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -self.rebalance_threshold and self.get_balance(root.right) > 0:
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

# Measure execution time for inserting the 500 flights
start_time = time.perf_counter()

# Create flights with flight number, departure time, origin, destination, price, and seat_number
flights_list = []
origins = ["New York", "Los Angeles", "Miami", "Houston", "San Francisco", "Austin", "Springfield", "Bloomington"]
destinations = ["Dallas", "New York", "Las Vegas", "San Diego", "Boston", "Chicago", "Peoria", "Providence"]
for i in range(1, 501):
    flight_no = 1000 + i  # Ensure unique flight numbers
    departure_time = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}"  # Random time
    origin = random.choice(origins)
    destination = random.choice(destinations)
    price = random.randint(100, 1000)               # Random price
    seat_number = random.randint(1, 50)             # Random seat number
    flights_list.append(Flight(flight_no, departure_time, origin, destination, price, seat_number))

# Insert flights into the AVL tree
for fli in flights_list:
    flight_tree.root = flight_tree.insert(flight_tree.root, fli.flight_no, fli)

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time for inserting flights: {execution_time} seconds")
