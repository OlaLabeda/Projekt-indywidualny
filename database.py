from read_passenger_data import read_from_file
from read_plane_data import read_from_plane_file

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
                self.data = read_from_file(file_handle)
        except FileNotFoundError:
            raise PathNotFound('Could not open data base')
        except PermissionError:
            raise PermissionError('No permission to open database')
        except IsADirectoryError:
            raise PathIsDirectory('The path is a directory')


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
