# Create a node class for individual seat on the flight
class SeatNode:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False                      # All the seats are available in the beginning
        self.next = None

# Create a collection of seats on a flight
class FlightSeatsList:
    def __init__(self, size = 10):
        self.head = None
        for index in range(size):
            self.add_seat("S" + str(index + 1))

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

    def book_seat(self, seat_number):
        """ Book a seat by changing its availability (is_booked) status to True. """
        current_seat = self.head
        book_successful = False
        while current_seat is not None:
            if current_seat.seat_number == seat_number:
                if current_seat.is_booked:
                    print("Seat is already booked.")
                    book_successful = False
                else:
                    current_seat.is_booked = True
                    print("Seat has been successfully booked.")
                    book_successful = True
                break
            current_seat = current_seat.next
        print("The selected seat is not found.")
        return book_successful

    def cancel_seat_booking(self, seat_number):
        """ Cancel a booking by changing the seat's availability (is_booked) status to False. """
        current_seat = self.head
        while current_seat is not None:
            if current_seat.seat_number == seat_number:
                if current_seat.is_booked:
                    current_seat.is_booked = False
                    print("Seat has been successfully canceled.")
                else:
                    print("Seat is already available.")
                return
            current_seat = current_seat.next
        print("The selected seat is not found.")
    
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
        
        return False
