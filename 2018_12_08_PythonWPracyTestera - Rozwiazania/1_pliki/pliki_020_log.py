# Stworz funkcje ktra dla kazdego slowa znalezionego w poprzednim zadaniu zaloguje je w pliku "moj_log.log"
#
# log = logging.getLogger("my_handler")
# log.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s %(message)s')
# handler = logging.XYZHandler()
# handler.setFormatter(formatter)
# log.addHandler(handler)
#

import logging
from pliki_011_text import get_words_from_file


def log_words():
    log = logging.getLogger("my_handler")
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    log.addHandler(handler)

    handler = logging.FileHandler("mylog.log")
    handler.setFormatter(formatter)
    log.addHandler(handler)

    known_words = get_words_from_file('resources/words.txt')
    words_to_check = get_words_from_file('resources/python_doc.txt')

    for word in words_to_check:
        if word not in known_words:
            log.error("There is no such a word: " + word)

log_words()