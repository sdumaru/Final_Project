""" Store a flight class to store information regarding a flight """

from flight_seats import FlightSeatsList
from waitlist import MaxHeapPriorityQueue

class Passenger:
    """ Passenger class to store passenger details """
    def __init__(self, name, passenger_id, priority):
        self.name = name
        self.passenger_id = passenger_id
        self.priority = priority
        self.seat_number = None

class Flight:
    """ Flight class which will be used in flight reservation system """
    def __init__(self, flight_no, departure_time, origin, destination, price, seat_numbers = 10):
        self.flight_no = flight_no
        self.departure_time = departure_time
        self.destination = destination
        self.origin = origin
        self.price = price
        self.seat_numbers = seat_numbers
        self.passengers = []
        self.seat_linked_list = FlightSeatsList(seat_numbers)
        self.waiting_list = MaxHeapPriorityQueue()

    def get_seat_list(self):
        """ Return the linked list of the seats allocation """
        return self.seat_linked_list
