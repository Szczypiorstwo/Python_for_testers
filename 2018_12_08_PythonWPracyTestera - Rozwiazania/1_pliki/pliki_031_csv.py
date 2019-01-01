# Stworz funkcje ktora przygotuje plik CSV
# Plik powinien zawierac wpisy obrazujace iloczyn kartezjanski wszystkich danych testowych
# Sprawdz dokumentacje! https://docs.python.org/3/library/itertools.html#itertools.product
# itertools.product()
#
# csv.DictWriter(csvfile, fieldnames)
# writer.writeheader()
# writer.writerow({'max_speed': str(entry[0]), 'min_speed': str(entry[1]), 'avg_speed': str(entry[2])})
#
# Sprawdz dokumentacje open() i parametr newline

import csv
import itertools

def create_csv_file():
    max_speed = [90, 100, 50, 30]
    min_speed = [10, 20, 15]
    avg_speed = [40, 30, 70]
    with open('speed.csv', 'w', newline='') as csvfile:
        fieldnames = ['max_speed', 'min_speed', "avg_speed"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for entry in itertools.product(max_speed, min_speed, avg_speed):
            writer.writerow({'max_speed': entry[0], 'min_speed': str(entry[1]), 'avg_speed': str(entry[2])})


create_csv_file()