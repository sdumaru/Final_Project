""" Linked lists to store the seats of the flight """

class SeatNode:
    """ Individual seat node which will be inserted to the linked list """
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.passenger_id = None
        self.is_booked = False                      # All the seats are available in the beginning
        self.next = None

# Create a collection of seats on a flight
class FlightSeatsList:
    """ Collection of seats in a flight """
    def __init__(self, size):
        self.head = None
        for index in range(size):
            self.add_seat(index + 1)

    def add_seat(self, seat_number):
        """ Add a new seat node to the linked list. 
            Seat should be added in the beginning. """
        new_seat = SeatNode(seat_number)
        if not self.head:
            self.head = new_seat
        else:
            current_seat = self.head
            while current_seat.next is not None:
                current_seat = current_seat.next
            current_seat.next = new_seat

    def book_seat(self, seat_number, passenger_id):
        """ Book a seat by changing its availability (is_booked) status to True. """
        current_seat = self.head
        while current_seat is not None:
            if current_seat.seat_number == seat_number:
                if current_seat.is_booked:
                    print(f"Seat {seat_number} is already booked.")
                else:
                    current_seat.is_booked = True
                    current_seat.passenger_id = passenger_id
                    print(f"Seat {seat_number} has been successfully booked.")
                return current_seat.is_booked
            current_seat = current_seat.next
        print("The selected seat is not found.")
        return False

    def cancel_seat_booking(self, seat_number):
        """ Cancel a booking by changing the seat's availability (is_booked) status to False. """
        current_seat = self.head
        while current_seat is not None:
            if current_seat.seat_number == seat_number:
                if current_seat.is_booked:
                    current_seat.is_booked = False
                    current_seat.passenger_id = None
                    print(f"Seat {seat_number} has been successfully canceled.")
                else:
                    print(f"Seat {seat_number} is already available.")
                return not current_seat.is_booked
            current_seat = current_seat.next
        print("The selected seat is not found.")
        return False

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
        """ Check there is any available seats in the flight """
        current_seat = self.head
        while current_seat is not None:
            if not current_seat.is_booked:
                return True
            current_seat = current_seat.next
        return False

# Usage example for seat linked list
flight_seats = FlightSeatsList(10)

# Showing seat availability before booking
print("Initial Seat Availability:")
flight_seats.show_seat_availability()

# Booking seat 3 and 5
flight_seats.book_seat(3, 1401)
flight_seats.book_seat(5, 1402)

# Showing seat availability after booking
print("\nSeat Availability after Booking:")
flight_seats.show_seat_availability()

# Canceling seat 5
flight_seats.cancel_seat_booking(5)

# Showing seat availability after canceling a booking
print("\nSeat Availability after Cancellation:")
flight_seats.show_seat_availability()
