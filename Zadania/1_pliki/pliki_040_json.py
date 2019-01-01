#
# Stworz funkcje wczytujaca plik widget.json do slownika

import json
from pprint import pprint

def get_widget():
    with open("resources/widget.json") as f:
        widget = json.load(f)
    return widget

w = get_widget()
pprint(w)
