# Zainstaluj mysqlclient
# Stworz klase odpowiedzialna za obsluge polaczenia z baza MqSql Wordpressa
# Bazując na metodzie print_owners z poprzedniego zadania stworz funkcje
# wypisujaca wszystkie posty (baza wordpress)
# https://github.com/PyMySQL/mysqlclient-python/blob/master/doc/user_guide.rst#mysqldb
# host="x.x.x.x", port=3306, user="test", passwd="test", db="wordpress"

import MySQLdb

class DbHandler:
    def print_post(self):
        conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="test", passwd="test", db="wordpress")
        with conn:
            c = conn.cursor()
            c.execute("SELECT post_content FROM wp_posts")
            x = c.fetchall()
            for wpis in x:
                print(wpis[0])


db = DbHandler()
db.print_post()
