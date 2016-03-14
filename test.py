
import sqlite3

def ajout(self):
    db = sqlite3.connect('DataBase.db')

    cursor = db.cursor()
    cursor.execute("""
    DROP TABLE contacts
    """)

    cursor.execute("""
    CREATE TABLE contacts(
        name TEXT,
        lastName TEXT,
        number INT,
        adress TEXT
    );
    """)


    info = self.editWho.text()
    cursor.execute("""
        INSERT INTO contacts(name) VALUES(?)""",(info,))


    cursor.execute("""
        SELECT name FROM contacts""")
    person = cursor.fetchall()
    db.commit()
    print(person)
