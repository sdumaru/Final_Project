
import flight_seats
from flights import Flight
from flight_collection import AVLTree

class BookingDetail:
    def __init__(self, customer_name, flight_no, destination, seat_no):
        self.customer_name = customer_name
        self.flight_no = flight_no
        self.destination = destination
        self.seat_no = seat_no

class FlightReservationSystem:
    
    # Hash Table for flight bookings
    # bookings[booking_id] = booking_details
    def __init__(self):
        self.root = None
        self.flights = AVLTree()
        self.passenger_info = {}

    # def add_airport(self, airport_code):
        # self.add_airport

    def add_flight(self, flight_number, departure_time, origin, destination, price, seats):
        flight = Flight(flight_number, departure_time, origin, destination, price, seats)
        self.flights.insert(self.root, flight_number, flight)
        print(f"Flight {flight_number} from {origin} to {destination} added with {seats} seats.")

    def find_flight(self, flight_number):
        return True
        # return self.flights.sea(flight_number, None)
    
    def reserve_seat(self, seat, flight_number, passenger_id, business_class=False):
        flight = self.find_flight(flight_number)
        if flight is None:
            print(f"Flight {flight_number} not found")
            return
        
        if flight.seat_linked_list.is_seat_available():
            waitlist_input = input("No available seats. Do you want to be on waiting list?")
            # Add to waiting list if yes otherwise return 
            return

        priority = 1 if business_class else 2
        flight.seat_linked_list.show_available_seat()
        while True:
            selected_seat = input("Select which seat would you like.")
            if flight.seat_linked_list.book_seat(selected_seat):
                break
        
        self.passenger_info[passenger_id] = BookingDetail("Sujan", flight_number, flight.destination, selected_seat)

    def cancel_reservation(self, passenger_id):
        if passenger_id in self.passenger_info:
            info = self.passenger_info[passenger_id]
            seat= info.seat_no
            flight_number = info.flight_number

            del self.passenger_info[passenger_id]

            flight = self.find_flight(flight_number)
            flight.seat_linked_list.cancel_seat_booking(seat)
            # Check the person in waiting line next and add them in that seat

        else:
            print(f"Passenger {passenger_id} not found.")

    def display_flights(self):
        print("Available flights (sorted by flight number):")
        for flight_number, flight in self.flights.items():
            print(f"Flight {flight_number}: {flight.origin} -> {flight.destination} at {flight.departure_time}")

# Example Usage
if __name__ == "__main__":
    flight_system = FlightReservationSystem()

    # Adding flights
    flight_system.add_flight("AA100", "08:00", "JFK", "LAX", 500, 15)
    flight_system.add_flight("UA200", "09:00", "JFK", "ORD", 400, 20)
    flight_system.add_flight("DL300", "10:00", "ORD", "LAX", 600, 25)
    flight_system.add_flight("AA400", "11:00", "DFW", "ATL", 300, 10)
    flight_system.add_flight("DL500", "12:00", "ATL", "JFK", 200, 5)
