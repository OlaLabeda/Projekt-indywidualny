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
                line = line.replace('\t', '')
                length_of_line = len(line)
                elements = 3
                while elements < length_of_line:
                    seats[key].append(line[elements-3:elements])
                    elements += 3
            line = f_path.readline()
            increment += 1

    return seats