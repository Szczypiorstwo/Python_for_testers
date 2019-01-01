# Uzupelnij funkcje execute_query tak by wykonywala zadane zapytanie
# Uzupelnij funkcję print_owners tak by wypisywala wszystkie osoby z bazy danych


import os
import sqlite3


class DBHandler:

    con = None

    def __init__(self, f):
        self.path = f
        self.__create_db()
        self.__create_tables()

    def __create_tables(self):
        try:
            self.__create_cars_table()
        except sqlite3.Error as e:
            print(e.args)
        try:
            self.__create_owners_table()
        except sqlite3.Error as e:
            print(e.args)

    def __create_db(self):
        if os.path.isfile(self.path):
            print("DB file already exists")
        else:
            sqlite3.connect(self.path).close()

    def __create_cars_table(self):
        con = sqlite3.connect(self.path)
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Speed INT)")
            cur.execute("INSERT INTO Cars VALUES(1,'Polonez',120)")
            cur.execute("INSERT INTO Cars VALUES(2,'Maluch',90)")
            cur.execute("INSERT INTO Cars VALUES(3,'Warszawa',90)")
            cur.execute("INSERT INTO Cars VALUES(4,'Syrena',70)")

    def __create_owners_table(self):
        persons = (
            (1, 'Adrian', 22),
            (2, 'Malgosia', 30),
            (3, 'Pawel', 55),
            (4, 'Kajtek', 80)
        )
        con = sqlite3.connect(self.path)
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE Owners(Id INT, Name TEXT, Age INT)")
            cur.executemany("INSERT INTO Owners VALUES(?, ?, ?)", persons)

    def print_owners(self):
        results = self.execute_query("SELECT * from Owners")
        for record in results:
            print(record[1])

    def execute_query(self, query):
        con = sqlite3.connect(self.path)
        with con:
            cur = con.cursor()
            cur.execute(query)
            results = cur.fetchall()
        return results


db = DBHandler('cars.db')
db.print_owners()
print(db.execute_query("SELECT * FROM Cars"))


