
import flight_seats
import flights

class BookingDetail:
    def __init__(self, customer_name, flight_no, destination, total_seats, seat_no):
        self.customer_name = customer_name
        self.flight_no = flight_no
        self.destination = destination
        self.total_seats = total_seats
        self.seat_no = seat_no

class FlightReservation:
    
    # Hash Table for flight bookings
    # bookings[booking_id] = booking_details
    def __init__(self):
        self.bookings = {}
