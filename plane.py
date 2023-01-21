class Plane:
    def __init__(self, plane_id, name,
                 length, height, wingspan,
                 hull_diameter, max_take_off_weight,
                 number_of_seats, engines,
                 speed, range, max_fuel, availabale_classes,
                 list_of_seats = {}):
        self._plane_id = plane_id
        self._name = name
        self._length = length
        self._height = height
        self._wingspan = wingspan
        self._hull_diameter = hull_diameter
        self._max_take_off_weight = max_take_off_weight
        self._number_of_seats = number_of_seats
        self._engines = engines
        self._speed = speed
        self._range = range
        self._max_fuel = max_fuel
        self._available_classes = availabale_classes
        self.list_of_seats = list_of_seats

    def plane_id(self):
        return self._plane_id

    def name(self):
        return self._name

    def length(self):
        return self._length

    def height(self):
        return self._height

    def wingspan(self):
        return self._wingspan

    def hull_diameter(self):
        return self._hull_diameter

    def max_take_off_weight(self):
        return self._max_take_off_weight

    def number_of_seats(self):
        return self._number_of_seats

    def engines(self):
        return self._engines

    def speed(self):
        return self._speed

    def range(self):
        return self._range

    def fuel(self):
        return self._max_fuel

    def available_classes(self):
        return self._available_classes

    def print_plane_info(self):
        print("Name: ", self.name().rjust(25))
        print("Length: ", self.length().rjust(25))
        print("Height: ", self.height().rjust(25))
        print("Wingspan: ", self.wingspan().rjust(25))
        print("Hull diameter: ", self.hull_diameter().rjust(25))
        print("Maximum take off weight: ", self.max_take_off_weight().rjust(25))
        print("Number of seats: ", self.number_of_seats().rjust(25))
        print("Engines: ", self.engines().rjust(25))
        print("Speed: ", self.speed().rjust(25))
        print("Range: ", self.range().rjust(25))
        print("Maxinum fuel: ", self._max_fuel().rjust(25))
        print("\n")
        # printowanie listy siedzen lol




