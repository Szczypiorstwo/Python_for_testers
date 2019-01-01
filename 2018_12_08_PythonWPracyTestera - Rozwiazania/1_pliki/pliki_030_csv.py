# Stworz funkcje wczytujaca rekokrdy z pliku csv do listy slownikow
# DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
import csv
from pprint import pprint


def read_csv_to_list(path):
    with open(path, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        print(reader.fieldnames)
        return [record for record in reader]


pprint(read_csv_to_list('resources/sales.csv'))
