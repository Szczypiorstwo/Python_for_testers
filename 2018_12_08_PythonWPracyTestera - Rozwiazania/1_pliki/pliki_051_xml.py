import xml.etree.ElementTree as ET

# Stworz funkcje ktora stworzy string w formacie xml:
# <Cars>
#   <car brand="Opel">
#       <model>Corsa</model>
#   </car>
# </Cars>


def create_xml():

    root = ET.Element("Cars")
    car = ET.SubElement(root, "car", {'brand': 'Opel'})
    model = ET.SubElement(car, 'model')
    model.text = "Corsa"
    tree = ET.ElementTree(root)
    print(ET.dump(tree))


if __name__ == "__main__":
    create_xml()