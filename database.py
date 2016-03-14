import sqlite3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QListWidget, QTextBrowser

db = sqlite3.connect('DataBase.db')

def ajouter(infos):
    cursor.execute("""
    INSERT INTO contacts(name, lastName) VALUES(?,?)""",("infos"))

def supprimer(infos):
    cursor.execute("""
    DELETE FROM contacts WHERE ["infos"])
    """)

def modifier(infos):
    cursor.execute("""
    UPDATE contacts
    SET column1 = value1, column2 = value2...., columnN = valueN
    WHERE [condition]
    """)

def creation():
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
    
    cursor.execute("""
    INSERT INTO contacts(name, lastName) VALUES(?,?)""",("tic", "tac",))

    cursor.execute("""
    SELECT name, lastName FROM contacts""")
    person = cursor.fetchone()
    db.commit()
    print(person)



if __name__ == '__main__':
        
    app = QApplication(sys.argv)

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
    
    cursor.execute("""
    INSERT INTO contacts(name, lastName) VALUES(?,?)""",("tic", "tac",))

        
    cursor.execute("""
    INSERT INTO contacts(name, lastName) VALUES(?,?)""",("mr", "mme",))

    cursor.execute("""
    INSERT INTO contacts(name, lastName) VALUES(?,?)""",("bonjour", "truc",))

    cursor.execute("""
    INSERT INTO contacts(name, lastName) VALUES(?,?)""",("kinder", "bueno",))

    cursor.execute("""
    INSERT INTO contacts(name, lastName) VALUES(?,?)""",("pingui", "kinder",))    
    
    cursor.execute("""
    SELECT name FROM contacts""")
    person = cursor.fetchall()
    db.commit()
    print(person)
        
    w = QWidget()
    aj = QPushButton('ajout',w)
    su = QPushButton('pop',w)
    bro = QLineEdit(w)
    liste = QListWidget(w)
    
    su.move(50,50)
    bro.move(450,50)

    liste.move(100,100)

    for row in person:
        liste.addItem(row[0]) 

    aj.clicked.connect( liste.addItem(bro.displayText()) )
        
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.showMaximized()
        
    sys.exit(app.exec_())
