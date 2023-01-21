from flight import Flight
import csv

class MalformFlightDataError(Exception):
    pass

class InvalidFlightError(Exception):
    def __init__(self, tokens):
        super().__init__("Invalid Flight Data detected")
        self.tokens = tokens

def read_from_flight_file(file_handle):
    flights = []
    reader = csv.DictReader(file_handle)
    try:
        for row in reader:
            flight_id = row['flight_id']
            go_from = row['go_from']
            go_to = row['go_to']
            date_from = row['date_from']
            date_to = row['date_to']
            hour_from = row['hour_from']
            hour_to = row['hour_to']
            gate_number = row['gate_number']
            plane_id = row['plane_id']
            plane_name = row['plane_name']
            if None in row.values():
                raise MalformFlightDataError('Missing column in file')
            try:
                flight = Flight(flight_id, go_from, go_to,
                                date_from, date_to,
                                hour_from, hour_to,
                                gate_number, plane_id,
                                plane_name)
            except Exception:
                raise InvalidFlightError(row)
            flights.append(flight)
    except csv.Error as e:
        raise MalformFlightDataError(str(e))
    return flights