""" Store a flight class to store information regarding a flight """

class Flight:
    """ Flight class which will be used in flight reservation system """
    def __init__(self, flight_no, destination, airline, price, seat_chain):
        self.flight_no = flight_no
        self.destination = destination
        self.airline = airline
        self.price = price
        self.seat_linked_list = seat_chain
