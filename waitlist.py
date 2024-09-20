""" Priority Queue to maintain the waitlist on the flight based on the highest priority """

# from flights import Passenger

class MaxHeapPriorityQueue:
    """ Maximum heap priority queue which will store highest priority passenger first """
    def __init__(self):
        self.heap = []

    def shift_up(self, index):
        """ Function to restore max heap property """
        parent_index = (index - 1) // 2

        # Make sure that the highest priority is at the root
        if index > 0 and self.heap[index].priority > self.heap[parent_index].priority:
            # Swap with parent if current node's priority is higher
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.shift_up(parent_index)

    def insert(self, passenger):
        """ Insert passenger into the waitlist """
        self.heap.append(passenger)
        self.shift_up(len(self.heap) - 1)

    def heap_maximum_element(self):
        """ Return the maximum element from the heap """
        if self.is_empty():
            raise IndexError("Maximum Heap Priority queue is empty.")
        return self.heap[0]

    def shift_down(self, index):
        """ Function to shift down the passenger based on the priority """
        heap_size = len(self.heap)
        left = 2 * index + 1                        # Left child index with parent index
        right = 2 * index + 2                       # Right child index with parent index

        # Check to see if the left child of root exists and if it does,
        # check to see if the priority is larger than the root.
        # Set the largest to the larger value index between left child and root
        if (left < heap_size) and (self.heap[left].priority > self.heap[index].priority):
            largest = left
        else:
            largest = index

        # Check to see if the right child of root exists and if it does,
        # check to see if the value is larger than the root.
        # Set the largest to the right child index in order to swap
        if (right < heap_size) and (self.heap[right].priority > self.heap[largest].priority):
            largest = right

        # If the largest is either left or right child, swap it with the root
        if largest is not index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]

            # Recursively heapify the affected subtree
            self.shift_down(largest)

    def extract_max(self):
        """ Function to get the passenger with the highest priority from the list """
        max_value = self.heap_maximum_element()         # Get the maximum priority passenger from the heap
        self.heap[0] = self.heap[-1]
        self.heap.pop()                                 # Remove the last passenger
        self.shift_down(0)                              # Get the highest priority passenger to top again

        return max_value

    def is_empty(self):
        """ Return if the waitlist is empty or not """
        return len(self.heap) == 0

# flight_waitlist = MaxHeapPriorityQueue()

# flight_waitlist.insert(Passenger("Sujan", 1400, 5))
# flight_waitlist.insert(Passenger("Zach", 1400, 3))
# flight_waitlist.insert(Passenger("Akku", 1400, 2))
# flight_waitlist.insert(Passenger("Kamal", 1400, 4))
# flight_waitlist.insert(Passenger("Max", 1400, 1))
# flight_waitlist.insert(Passenger("Caleb", 1400, 4))

# # Check queue state
# print("Queue before extracting lowest element:")
# for i in flight_waitlist.heap:
#     print("Task ID: ", i.name, " Priority: ", i.priority)

# # Extract heap_minimum_element
# print("Extracted passenger:", flight_waitlist.extract_max().name)   # Should extract Sujan
# print("Extracted passenger:", flight_waitlist.extract_max().name)   # Should extract Kamal
# print("Extracted passenger:", flight_waitlist.extract_max().name)   # Should extract Caleb

# # Check queue state
# print("Queue after extraction:")
# for i in flight_waitlist.heap:
#     print("Task ID: ", i.name, " Priority: ", i.priority)

# # Check if empty
# print("Is waitlist empty?", flight_waitlist.is_empty())

# print("Extracted passenger:", flight_waitlist.extract_max().name)   # Should extract Zach
# print("Extracted passenger:", flight_waitlist.extract_max().name)   # Should extract Akku
# print("Extracted passenger:", flight_waitlist.extract_max().name)   # Should extract Max

# # Check if empty
# print("Is waitlist empty?", flight_waitlist.is_empty())
