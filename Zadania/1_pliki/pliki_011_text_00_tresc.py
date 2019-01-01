# ZNAJDŹ LIETROWKI
# Wypisz wszystkie solowa z pliku python_doc.txt, ktore nie znajduja sie w slowniku words.txt
# https://docs.python.org/3/library/stdtypes.html#string-methods

# Stworz funkcje ktora podzieli plik na slowa i zapisze je w liscie
# - Wczytaj tresc pliku
# - Zamien wszystkie litery na male
# - Zastap wszystkie znaki niebedace literami znakiem spacji:
# regex = re.compile('[^a-zA-Z]')
# po_zmiane = regex.sub(' ', przed_zmiasna)
#
# - Podziel zmienna na pojedyncze slowa

# 8. spradz czy slowa znajduja sie w slowniku, wypisz jezeli nie

# *9. Wypisz linie i pozycje slowa

def get_words_from_file(file_to_read):
    #TODO
    pass

known_words = get_words_from_file('resources/words.txt')
words_to_check = get_words_from_file('resources/python_doc.txt')

for word in words_to_check:
    #TODO
    pass