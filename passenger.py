class   Passenger:
    """
        class person contains
        : param name: persons name
        : param surname
        : param ticket_number: number to identify bought ticket
        : phone number

    """
    def __init__(self, id, name, surname, ticket_number, flight_id, phone_number, seat):
        self._id = id
        self._name = name
        self._surname  = surname
        self._ticket_number = ticket_number
        self._phone_number = phone_number
        self._flight_id = flight_id
        self._seat = seat

    def __str__(self):
        id = self.id()
        name = self.name()
        surname = self.surname()
        ticket_number = self.ticket_number()
        phone_number = self.phone_number()
        flight_id = self.flight_id()
        return f'{id}, {name} {surname}, {ticket_number}, {flight_id}'

    def set_seat(self, new_seat):
        self._seat = new_seat

    def name(self):
        return self._name

    def surname(self):
        return self._surname

    def id(self):
        return self._id

    def ticket_number(self):
        return self._ticket_number

    def phone_number(self):
        return self._phone_number

    def flight_id(self):
        return self._flight_id

    def seat(self):
        return self._seat