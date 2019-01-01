import xml.etree.ElementTree as ET
import csv

# Wczytaj dane z pliku resources/sales.csv i zapisz je jako plik XML w podanym formacie:
# <Transtactions>
#   <Transaction date="1/2/09 6:17">
#       <product>Product1</product>
#       <price>1200</price>
#       <location>
#           <country>United Kingdom</country>
#           <city>Basildon</city>
#       </location>
#   </Transaction>
# </Transtactions>

def create_xml():
    root = ET.Element("Transtactions")
    tree = ET.ElementTree(root)
    with open('resources/sales.csv', newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        print(reader.fieldnames)
        for row in reader:
            trans = ET.SubElement(root, 'Transaction', {'date': row['Transaction_date']})
            product = ET.SubElement(trans, 'product')
            product.text = row['Product']
            price = ET.SubElement(trans, 'price')
            price.text = row['Price']
            location = ET.SubElement(trans, 'location')
            country = ET.SubElement(location, 'country')
            country.text = row['Country']
            city = ET.SubElement(location, 'city')
            city.text = row['City']
    tree.write("new.xml", encoding="us-ascii", xml_declaration=True)

create_xml()