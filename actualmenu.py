from database import DatabasePerson, DatabasePlane, DatabaseFlight
from passenger import Passenger
from plane import Plane
from flight import Flight
from read_seats import read_plane_from_plane_file
import os


def check_input_data(name, surname, ticket_number, phone_number, list_of_passengers):
    for passengers in list_of_passengers:
        if (passengers.name() == name and
            passengers.surname() == surname and
            passengers.ticket_number() == ticket_number and
            passengers.phone_number() == phone_number):
                return {'id': passengers.id(), 'flight': passengers.flight_id(),
                        'seat': passengers.seat()}
    return {}


def flight_info(id, list_of_flights):
    for planes in list_of_flights:
        if (planes.flight_id() == id):
            return planes

def edited_passenger(ticket_number, list_of_passengers):
    for passenger in list_of_passengers:
        if (passenger.ticket_number() == ticket_number):
            return passenger


def boarding_gate_info(flight_data):
    gate_number = flight_data.gate_number()
    boarding_till = flight_data.boarding_till()
    first_part = f'Number of the gate: {gate_number.rjust(23)}\n'
    second_part = f'Boarding process till: {boarding_till.rjust(20)}'
    return first_part + second_part


def flight_data_to_print(flight_data):
    place_from = flight_data.go_from()
    place_to = flight_data.go_to()
    departure_date = flight_data.date_from()
    arrival_date = flight_data.date_to()
    departure_time = flight_data.hour_from()
    arrival_time = flight_data.hour_to()
    plane_name = flight_data.plane_name()
    place = 'From:'.ljust(20) + place_from.rjust(10) + ' '.ljust(10) + 'To:'.ljust(20) + place_to.rjust(10)
    date = 'Departure_date:'.ljust(20) + departure_date.rjust(10) + " ".ljust(10) + 'Arrival_date:'.ljust(20) + arrival_date.rjust(10)
    time = 'Departure_time:'.ljust(20) + departure_time.rjust(10) + " ".ljust(10) + 'Arrival_time:'.ljust(20) + arrival_time.rjust(10)
    return place + '\n' + date + '\n' + time + '\n' + 'Plane name:'.ljust(20) + plane_name.rjust(50)


def boarding_card(passengers_data, flight_data, seat_number, seat_class):
    name = passengers_data.name()
    surname = passengers_data.surname()
    seat = 'Seat number:'.ljust(20) + seat_number.rjust(10) + ' '.ljust(10) + 'Class:'.ljust(20) + seat_class.rjust(10)
    passenger = 'Name:'.ljust(20) + name.rjust(10) + ' '.ljust(10) + 'Surname:'.ljust(20) + surname.rjust(10)
    return seat + '\n' + passenger + '\n' + flight_data_to_print(flight_data)


def seat_data(which_class_size, passenger):
        if which_class_size == 11:
            seat_class = 'business'
            seat_number = passenger.seat()[8:12]
        elif which_class_size == 18:
            seat_class = 'economy-premium'
            seat_number = passenger.seat()[15:18]
        else:
            seat_class = 'economy'
            seat_number = passenger.seat()[7:11]
        return (seat_class, seat_number)


def plane_data(plane_name, list_of_planes):
    for planes in list_of_planes:
        if planes.name() == plane_name:
            return planes


def plane_info_to_print(plane_data):
        id = plane_data.plane_id()
        name = plane_data.name()
        len = plane_data.length()
        height = plane_data.height()
        wing = plane_data.wingspan()
        diam = plane_data.hull_diameter()
        weight = plane_data.max_take_off_weight()
        seats = plane_data.number_of_seats()
        engines = plane_data.engines()
        speed = plane_data.speed()
        p_range = plane_data.range()
        p_fuel = plane_data.fuel()
        s1 = 'Plane id: '.ljust(20) + id.rjust(15) + '\n' + 'Name: '.ljust(20) + name.rjust(15) + '\n'
        s2 = 'Length: '.ljust(20) + len.rjust(15) + '\n' + 'Height: '.ljust(20) + height.rjust(15) + '\n'
        s2 = 'Wingspan: '.ljust(20) + wing.rjust(15) + '\n' + 'Hull diameter: '.ljust(20) + diam.rjust(15) + '\n'
        s3 = 'Weight: '.ljust(20) + weight.rjust(15) + '\n' + 'Number of seats: '.ljust(20) + seats.rjust(15) + '\n'
        s4 = 'Engines: '.ljust(20) + engines.rjust(15) + '\n' + 'Speed: '.ljust(20) + speed.rjust(15) + '\n'
        s5 = 'Range: '.ljust(20) + p_range.rjust(15) + '\n' + 'Fuel: '.ljust(20) + p_fuel.rjust(15) + '\n'
        return '\n' + s1 + s2 + s3 + s4 + s5

def taken_seats(list_of_passengers, flight_id):
    list_of_taken_seats = {}
    for passenger in list_of_passengers:
        if (flight_id == passenger.flight_id()):
            which_class_size = len(passenger.seat())
            seat_info = seat_data(which_class_size, passenger)
            seat_class = seat_info[0]
            seat_number = seat_info[1]
            if seat_class in list_of_taken_seats.keys():
                list_of_taken_seats[seat_class].append(seat_number)
            else:
                list_of_taken_seats[seat_class] = []
                list_of_taken_seats[seat_class].append(seat_number)
    return list_of_taken_seats


def available_seats(plane_seats, list_of_taken_seats):
    list_of_available_seats = {}
    for keys in plane_seats.keys():
        for elements in plane_seats[keys]:
            for lists in elements:
                if lists not in list_of_taken_seats[keys]:
                    if keys in list_of_available_seats.keys():
                        list_of_available_seats[keys].append(lists)
                    else:
                        list_of_available_seats[keys] = []
                        list_of_available_seats[keys].append(lists)
    return list_of_available_seats


def main():
    list_of_passengers = DatabasePerson
    list_of_passengers.load_from_file(list_of_passengers,
                                      "passengers_data.txt")
    if_logged_in = {}
    while (len(if_logged_in) == 0):
        name = input('Enter Your name: ')
        surname = input('Enter Your surname: ')
        ticket_number = input('Enter Your ticket number: ')
        phone_number = input('Enter Your phone_number: ')
        if_logged_in = check_input_data(name, surname,
                                    ticket_number, phone_number,
                                    list_of_passengers.data)
        if (len(if_logged_in) != 0):
            passenger = Passenger(if_logged_in['id'], name,
                                  surname, ticket_number,
                                  if_logged_in['flight'], phone_number,
                                  if_logged_in['seat']
                                  )
            print("Entered data is correct!")
            os.system('cls')
        else:
            print("Entered data is incorrect.")
            if_continue = input("Press a if u want to try again ")
            if (if_continue != 'a' and if_continue != 'A'):
                return 0


    if (if_logged_in['id']):
        list_of_planes = DatabasePlane
        list_of_planes.load_from_file(list_of_planes,
                                      "plane_data.txt")

        list_of_flights = DatabaseFlight
        list_of_flights.load_from_file(list_of_flights,
                                       "flights_data.txt")

        flight_informations =  flight_info(passenger.flight_id(),
                                           list_of_flights.data)

        file_with_plane_seats = f'{flight_informations.plane_name()}.txt'
        plane_seats = read_plane_from_plane_file(file_with_plane_seats)

        which_class_size = len(passenger.seat())
        seat_info = seat_data(which_class_size, passenger)

        seat_class = seat_info[0]
        seat_number = seat_info[1]

        print(f'You bought a ticket for {seat_class} class')
        print(f"Number of Your seat: {seat_number}")

        plane_info = Plane
        plane_info = plane_data(flight_informations.plane_name(), list_of_planes.data)

        if_chosen = 0
        while if_chosen == 0:
            print("Press:")
            print("1 if You want to change the class or number of the seat")
            print("2 if You want to print Your boarding pass")
            print("3 if You want to recieve boarding gate info")
            print("4 if You want to recieve plane and flight info")
            if_chosen = input()
            os.system('cls')
            if if_chosen == '1':
                list_of_taken_seats = taken_seats(list_of_passengers.data, passenger.flight_id())
                list_of_available_seats = available_seats(plane_seats, list_of_taken_seats)
                if list_of_available_seats:
                    print('Available seats: ')
                    for keys in list_of_available_seats.keys():
                        print(f'In {keys} class:')
                        print(list_of_available_seats[keys])

                    correct_seat_num = 0
                    while correct_seat_num == 0:
                        print('Type in the seat number You would like to change to: ')
                        seat_change = input()
                        if_among_available = 0
                        for keys in list_of_available_seats.keys():
                            for values in list_of_available_seats[keys]:
                                if seat_change == values:
                                    new_class = keys
                                    if_among_available  = 1
                                    break

                        if if_among_available == 1:
                            seat_number = seat_change
                            seat_class = new_class
                            new_seat = new_class + seat_change
                            passenger.set_seat(new_seat)
                            list_of_passengers.save_to_file(list_of_passengers, 'passengers_data.txt')
                            list_of_passengers.load_from_file(list_of_passengers, 'passengers_data.txt')
                            passenger = edited_passenger(passenger.ticket_number(), list_of_passengers.data)
                            correct_seat_num = 1
                            print('You successfully schanged Your seat')

                        if not if_among_available:
                            print('Incorrect data. Press a if You want to try again')
                            again = input()
                            if again == 'a' or again == 'A':
                                correct_seat_num = 0
                            else:
                                break
                else:
                    print('There is no available seats left')
                print("If You want to return to menu press y")
                if_return = input()
                if if_return == 'y' or if_return =='Y':
                    if_chosen = 0
                else:
                    return 0
            elif if_chosen == '2':
                passenger = edited_passenger(passenger.ticket_number(), list_of_passengers.data)
                print(boarding_card(passenger, flight_informations, seat_number, seat_class))
                boarding_card_data = open("boarding_card.txt", "w")
                boarding_card_data.write(boarding_card(passenger, flight_informations, seat_number, seat_class))
                boarding_card_data.close()
                print("\nIf You want to return to menu press y")
                if_return = input()
                if if_return == 'y' or if_return =='Y':
                    if_chosen = 0
                else:
                    return 0
            elif if_chosen == '3':
                print(boarding_gate_info(flight_informations))
                print("\nIf You want to return to menu press y")
                if_return = input()
                if if_return == 'y' or if_return =='Y':
                    if_chosen = 0
                else:
                    return 0
            elif if_chosen == '4':
                print(flight_data_to_print(flight_informations))
                print(plane_info_to_print(plane_info))
                print("\nIf You want to return to menu press y")
                if_return = input()
                if if_return == 'y' or if_return =='Y':
                    if_chosen = 0
                else:
                    return 0
            else:
                if_continue = input("There's no such option, press a to try again: ")
                print("\nIf You want to return to menu press y")
                if_return = input()
                if if_return == 'y' or if_return =='Y':
                    if_chosen = 0
                else:
                    return 0


if __name__ == "__main__":
    main()