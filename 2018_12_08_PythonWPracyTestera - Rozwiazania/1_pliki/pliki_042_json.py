# Stworz funkcje konwertujaca plik menu.json do obiektu klasy Menu.
#
# Struktura obiektu powinna wygladac nastepujaco:
#
# class Menu:
#     header = "string"
#     items = ["string1", "string2", "string3"]
#
# pola klasy powinny zostac wygenerowane automatycznie na podstawie zawartosci slownika stworzonego z pliku json
#
#
# przydatny moze okazac sie parametr object_hook

import json

with open('resources/menu.json') as f:
    menu = json.load(f)


class Menu:
    def __init__(self, json):
        if 'menu' in json.keys():
            self.__dict__ = json['menu'].__dict__
        else:
            self.__dict__ = json


widgetObj = json.loads(json.dumps(menu), object_hook=Menu)
pass



