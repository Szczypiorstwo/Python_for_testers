# Napisz funkcje znajdującą bledy wystepujace pomiedzy zadanym czasem

# Otworz plik log
# Wczytaj jego zawartosc do listy
# Zamien liste na slownik, w ktorym kluczem bedzie data
# datetime.strptime(string_date, '%d/%b/%Y:%H:%M:%S')
# Wypisz widomosci zawierajace bledy pomiedzy zadanymi godzinami

from datetime import datetime


def get_date(date_str):
    datetime_object = datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S')
    return datetime_object


def get_date_from_line(line):
    str_date = line.split()
    str_date = str_date[1]
    return get_date(str_date[1:])


def convert_log_to_dictionary(log):
    my_dict = {}
    log_list = []
    with open(log) as f:
        log_list += f.readlines()
    for log_entry in log_list:
        my_dict[get_date_from_line(log_entry)] = log_entry
    return my_dict


def get_errors():
    start_date = get_date("07/Mar/2004:16:31:00")
    end_date = get_date("07/Mar/2004:17:1:59")

    log_dict = convert_log_to_dictionary("resources/logfile.log")
    for key, line in log_dict.items():
        if start_date <= key <= end_date:
            if "ERROR" in line:
                print(line)

get_errors()



