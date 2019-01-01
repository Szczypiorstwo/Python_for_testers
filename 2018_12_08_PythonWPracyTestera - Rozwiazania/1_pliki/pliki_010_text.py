# Stworz funkcje wypisujaca kraje z ktorych pochadza osoby wymienione w pliku humans.txt


def print_countries():
    all_lines = []
    with open("resources/humans.txt") as f:
        for line in f:
            all_lines.append(line)

    countries = set()
    for line in all_lines:
        if any(title in line for title in ["Location", "From"]):
            countries.add(line.replace('/', ',').replace(':', ',').split(',')[-1].strip())

    print(countries)


if __name__ == "__main__":
    print_countries()


