from passenger import Passenger
import csv

class MalformPassengerDataError(Exception):
    pass

class InvalidPassengerError(Exception):
    def __init__(self, tokens):
        super().__init__("Invalid Passenger Data detected")
        self.tokens = tokens

def read_from_file(file_handle):
    passengers = []
    reader = csv.DictReader(file_handle)
    try:
        for row in reader:
            id = row['id']
            name = row['name']
            surname = row['surname']
            ticket_number = row['ticket_number']
            flight_id = row['flight_id']
            phone_number = row['phone_number']
            seat = row['seat']
            if None in row.values():
                raise MalformPassengerDataError('Missing column in file')
            try:
                passenger = Passenger(id, name, surname, ticket_number, flight_id, phone_number, seat)
            except Exception:
                raise InvalidPassengerError(row)
            passengers.append(passenger)
    except csv.Error as e:
        raise MalformPassengerDataError(str(e))
    return passengers