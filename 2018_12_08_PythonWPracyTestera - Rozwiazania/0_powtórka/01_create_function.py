# Stworz funkcje ktora jako parametr przyjmuje lancuch znakow
# i zwroci slownik z dwoma pozycjami:
# klucze: "samogloski" i "spolgloski"
# wartosci: lista samoglosek i lista spolglosek


#print(foo("Ala ma kota"))

# {"samogloski": ["A", "a", "a", "o", "a"],
#  "spolgloski": ["l", "m", "k", "t"]}

from pprint import pprint

vowels = "samogloski"
consonants = "consonants"

def get_phones(my_str):
    phones = {
        vowels: [],
        consonants: []
    }
    for char in my_str.lower():
        if char in ['a', 'e', 'i', 'o', 'u', 'y']:
            phones[vowels].append(char)
        else:
            phones[consonants].append(char)
    pprint(phones)


if __name__ == "__main__":
    get_phones("Python w zyciu testera")
