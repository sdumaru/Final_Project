""" Store a flight class to store information regarding a flight """

from flight_seats import FlightSeatsList

class Flight:
    """ Flight class which will be used in flight reservation system """
    def __init__(self, flight_no, departure_time, origin, destination, price, seat_numbers = 10):
        self.flight_no = flight_no
        self.destination = destination
        self.origin = origin
        self.price = price
        self.seat_numbers = seat_numbers
        self.seat_linked_list = FlightSeatsList(seat_numbers)

