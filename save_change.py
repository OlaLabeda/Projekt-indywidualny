import csv

def write_to_file(file_handle, passengers):
    writer = csv.DictWriter(file_handle, ['id', 'name', 'surname', 'ticket_number', 'flight_id', 'phone_number', 'seat'])
    writer.writeheader()
    for passenger in passengers:
        id = passenger.id()
        name = passenger.name()
        surname = passenger.surname()
        ticket_number = passenger.ticket_number()
        flight_id = passenger.flight_id()
        phone_number = passenger.phone_number()
        seat = passenger.seat()
        writer.writerow({
            'id': id,
            'name': name,
            'surname': surname,
            'ticket_number': ticket_number,
            'flight_id': flight_id,
            'phone_number': phone_number,
            'seat': seat
        })