from read_passenger_data import read_from_passenger_file
from read_plane_data import read_from_plane_file
from read_flight_data import read_from_flight_file
from save_change import write_to_file


class PathNotFound(FileNotFoundError):
    pass

class PermissionError(PermissionError):
    pass

class PathIsDirectory(IsADirectoryError):
    pass

class DatabasePerson:
    def __init__(self):
        self.data = []

    def load_from_file(self, path):
        try:
            with open(path, 'r') as file_handle:
                self.data = read_from_passenger_file(file_handle)
        except FileNotFoundError:
            raise PathNotFound('Could not open data base')
        except PermissionError:
            raise PermissionError('No permission to open database')
        except IsADirectoryError:
            raise PathIsDirectory('The path is a directory')


    def save_to_file(self, path):
        try:
            with open(path, 'w') as file_handle:
                write_to_file(file_handle, self.data)
        except FileNotFoundError:
            raise PathNotFound('Could not open database')
        except PermissionError:
            msg = 'You dont have the permission to open database'
            raise PermissionError(msg)
        except IsADirectoryError:
            raise PathIsDirectory('can only work on files')


class DatabasePlane:
    def __init__(self):
        self.data = []

    def load_from_file(self, path):
        try:
            with open(path, 'r') as file_handle:
                self.data = read_from_plane_file(file_handle)
        except FileNotFoundError:
            raise PathNotFound('Could not open data base')
        except PermissionError:
            raise PermissionError('No permission to open database')
        except IsADirectoryError:
            raise PathIsDirectory('The path is a directory')


class DatabaseFlight:
    def __init__(self):
        self.data = []

    def load_from_file(self, path):
        try:
            with open(path, 'r') as file_handle:
                self.data = read_from_flight_file(file_handle)
        except FileNotFoundError:
            raise PathNotFound('Could not open data base')
        except PermissionError:
            raise PermissionError('No permission to open database')
        except IsADirectoryError:
            raise PathIsDirectory('The path is a directory')

