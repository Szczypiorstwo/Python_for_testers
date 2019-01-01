# Napisz funkcje znajdującą bledy wystepujace pomiedzy zadanym czasem

# Otworz plik log
# Wczytaj jego zawartosc do listy
# Zamien liste na slownik, w ktorym kluczem bedzie data
# datetime.strptime(string_date, '%d/%b/%Y:%H:%M:%S') - dokumentacja
# Wypisz widomosci zawierajace bledy pomiedzy zadanymi godzinami

from datetime import datetime


def get_date(date_str):
    #TODO
    pass


def get_date_from_line(line):
    #TODO
    pass

def convert_log_to_dictionary(log):
    #TODO
    pass


def get_errors():
    start_date = get_date("07/Mar/2004:16:31:00")
    end_date = get_date("07/Mar/2004:17:1:59")

    for key, line in convert_log_to_dictionary("resources/logfile.log").items():
        #TODO
        pass

get_errors()
