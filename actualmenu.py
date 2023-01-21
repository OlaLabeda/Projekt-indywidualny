from database import DatabasePerson, DatabasePlane, DatabaseFlight
from passenger import Passenger
from plane import Plane
from flight import Flight
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

def boarding_gate_info(flight_data):
    gate_number = flight_data.gate_number()
    boarding_till = flight_data.boarding_till()
    first_part = f'Number of the gate: {gate_number.rjust(23)}\n'
    second_part = f'Boarding process till: {boarding_till.rjust(20)}'
    return first_part + second_part


def fligh_data_to_print(flight_data):
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

        flight_informations =  flight_info(passenger.flight_id(), list_of_flights.data)
        print(f'passengers plane: {flight_informations.plane_name()}')



        which_class_size = len(passenger.seat())
        # class business => 8 letters or economy => 7 letters
        # nummber of a seat always has 3 signs
        # if length of a string  = 11 => business else economy
        if which_class_size == 11:
            seat_class = 'business'
            seat_number = passenger.seat()[8:11]
        elif which_class_size == 18:
            seat_class = 'economy-premium'
            seat_number = passenger.seat()[15:18]
        else:
            seat_class = 'economy'
            seat_number = passenger.seat()[7:10]

        if_is_next_to_the_window = 0
        # chyba najpierw tu pobiore plane dats
        # space for the checking function
        #
        print(f'You bought a ticket for {seat_class} class')
        print(f"Number of Your seat: {seat_number}")
        if if_is_next_to_the_window:
            print('Your sit is next to the window')
        else:
            print("Your sit is not next to the window")

        if_chosen = 0
        while if_chosen == 0:
            os.system('cls')
            print("Press:")
            print("1 if You want to change the class or number of the seat")
            print("2 if You want to print Your boarding pass")
            print("3 if You want to order the help of an assistant")
            print("4 if You want to recieve boarding gate info")
            print("5 if You want to recieve plane and flight info")
            if_chosen = input()
            os.system('cls')
            if if_chosen == '1':
                print("If You want to return to menu press y")
                if_return = input()
                if if_return == 'y' or if_return =='Y':
                    if_chosen = 0
                else:
                    return 0
            elif if_chosen == '2':
                print(2)
            elif if_chosen == '3':
                print(3)
            elif if_chosen == '4':
                print(boarding_gate_info(flight_informations))
                print("\nIf You want to return to menu press y")
                if_return = input()
                if if_return == 'y' or if_return =='Y':
                    if_chosen = 0
                else:
                    return 0
            elif if_chosen == '5':
                print(fligh_data_to_print(flight_informations))
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