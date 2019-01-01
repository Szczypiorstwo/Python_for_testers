# Stworz funkcje ktora policzy srednia cene potraw z pliku menu.xml
# https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.iter

import xml.etree.ElementTree as ET

def get_avg_price(path):
    #TODO


print("{:.4f}".format(get_avg_price("resources/menu.xml")))