import csv

def read_plane_from_plane_file(path_to_file):
    seats = {}
    with open(path_to_file) as f_path:
        line = f_path.readline()
        increment = 1
        key = 0
        while line:
            line = line.strip()
            if (line == 'business' or line == 'economy'
                or line == 'economy-premium'):
                seats[line] = []
                key = line
            else:
                line = line.replace('\n', '')
                line = line.replace('\t', ' ')
                line = line.split()
                length_of_line = len(line)
                seats[key].append(line)
            line = f_path.readline()
            increment += 1

    return seats
