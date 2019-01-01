import xml.etree.ElementTree as ET

# Stworz funkcje ktora policzy srednia cene potraw z pliku menu.xml
# https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.iter

def get_avg_price(f):
    tree = ET.parse(f)
    prices = []
    for elem in tree.iter('price'):
        prices.append(float(elem.text[1:]))
    return sum(prices)/len(prices)


if __name__ == "__main__":
    print("{:4.4f}".format(get_avg_price('resources/menu.xml')))