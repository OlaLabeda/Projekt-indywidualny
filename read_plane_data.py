from seats_in_a_plane import Plane
import csv

class MalformPlaneDataError(Exception):
    pass

class InvalidPlaneError(Exception):
    def __init__(self, tokens):
        super().__init__("Invalid Plane Data detected")
        self.tokens = tokens

def read_from_plane_file(file_handle):
    planes = []
    reader = csv.DictReader(file_handle)
    try:
        for row in reader:
            plane_id = row['plane_id']
            name = row['name']
            length = row['length']
            height = row['height']
            wingspan = row['wingspan']
            hull_diameter = row['hull_diameter']
            max_take_off_weight = row['max_take_off_weight']
            number_of_seats = row['number_of_seats']
            engines = row['engines']
            speed = row['speed']
            range = row['range']
            max_fuel = row['max_fuel']
            available_classes = row['available_classes']
            if None in row.values():
                raise MalformPlaneDataError('Missing column in file')
            try:
                plane = Plane(plane_id, name, length,
                              height, wingspan, hull_diameter,
                              max_take_off_weight, number_of_seats,
                              engines, speed, range, max_fuel,
                              available_classes, None)
            except Exception:
                raise InvalidPlaneError(row)
            planes.append(plane)
    except csv.Error as e:
        raise MalformPlaneDataError(str(e))
    return planes