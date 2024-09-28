""" Linked lists to store the seats of the flight """

import time

class SeatNode:
    """ Individual seat node which will be inserted to the linked list """
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.passenger_id = None
        self.is_booked = False                  # All the seats are available in the beginning
        self.next = None
        self.prev = None

# Create a collection of seats on a flight
class FlightSeatsList:
    """ Collection of seats in a flight """
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.seat_map = {}                      # Dictionary to map seat numbers for quick lookup
        for index in range(1, size + 1):
            self.add_seat(index)

    def add_seat(self, seat_number):
        """ Add a new seat node to the linked list. """
        new_seat = SeatNode(seat_number)
        self.seat_map[seat_number] = new_seat   # Add to seat map for quick lookup
        if not self.head:
            self.head = self.tail = new_seat
        else:
            self.tail.next = new_seat
            new_seat.prev = self.tail           # Set previous pointer to the current tail
            self.tail = new_seat                # Update the tail to the new seat

    def book_seat(self, seat_number, passenger_id):
        """ Book a seat by changing its availability status to True """
        seat_node = self.seat_map.get(seat_number)

        if seat_node is None:
            print(f"Seat {seat_number} does not exist.")
            return False

        if seat_node.is_booked:
            print(f"Seat {seat_number} is already booked.")
            return False

        # Book the seat
        seat_node.is_booked = True
        seat_node.passenger_id = passenger_id
        # print(f"Seat {seat_number} successfully booked for passenger {passenger_id}.")
        return True

    def cancel_seat_booking(self, seat_number):
        """ Cancel a booking by changing the seat's availability status to False """
        seat_node = self.seat_map.get(seat_number)

        if seat_node is None:
            print(f"Seat {seat_number} does not exist.")
            return False

        if not seat_node.is_booked:
            print(f"Seat {seat_number} is already available.")
            return False

        # Cancel the booking
        seat_node.is_booked = False
        seat_node.passenger_id = None
        # print(f"Seat {seat_number} successfully canceled.")
        return True

    def show_seat_availability(self):
        """ Display the availability of all seats. """
        current_seat = self.head
        while current_seat is not None:
            if current_seat.is_booked:
                status = "Booked"
            else:
                status = "Available"
            print(f"Seat {current_seat.seat_number}: {status}")
            current_seat = current_seat.next

    def is_seat_available(self):
        """ Check if there are any available seats in the flight """
        # Iterate over the seat_map for efficient checking
        return any(not seat.is_booked for seat in self.seat_map.values())


# Measure execution time for adding, booking seats and canceling booking
start_time = time.perf_counter()
flight_seats = FlightSeatsList(1000)

flight_seats.book_seat(300, 1401)
flight_seats.book_seat(500, 1402)

flight_seats.cancel_seat_booking(500)

end_time = time.perf_counter()
execution_time = end_time - start_time
# print(f"Total execution time: {execution_time} seconds")
