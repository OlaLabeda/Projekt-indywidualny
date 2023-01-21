from database import DatabasePerson
from passenger import Passenger
from seats_in_a_plane import Plane
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

       # if (if_logged_in['id']):
    #    list_of_planes = DatabasePlane
     #       list_of_planes.load_from_file(list_of_planes,
      #                                "plane_data.txt")

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
            print("Press:")
            print("1 if You want to change the class or number of the seat")
            print("2 if You want to print Your boarding pass")
            print("3 if You want to order the help of an assistant")
            print("4 if You want to recieve boarding gate info")
            print("5 if You want to recieve plane info")
            if_chosen = input()
            if if_chosen == 1:
                print("If You want to return to menu press y, else press n")

            elif if_chosen == 2:
                pass
            elif if_chosen == 3:
                pass
            elif if_chosen == 4:
                pass
            elif if_chosen == 5:
                pass
            else:
                pass

if __name__ == "__main__":
    main()