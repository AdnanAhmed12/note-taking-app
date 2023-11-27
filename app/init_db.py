import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()




cur.execute("INSERT INTO notes (id, title, description,color) VALUES (?, ?, ?, ?)",
            ('1', 'Omega Case', 'Remember to finish project by monday 1pm','pink')
            )

cur.execute("INSERT INTO notes (id, title, description,color) VALUES (?, ?, ?, ?)",
            ('2', 'reading list', 'Remember to finish HP 3','lightblue')
)
cur.execute("INSERT INTO kategories (katID, name,color) VALUES (?, ?, ?)",
            ('1','Food','pink')

)
cur.execute("INSERT INTO kategories (katID, name,color) VALUES (?, ?, ?)",
            ("2","Household","blue")

)
cur.execute("INSERT INTO kategories (katID, name,color) VALUES (?, ?, ?)",
            ("3","snacks","yellow")

)

cur.execute("INSERT INTO users (uid, username,password) VALUES (?, ?, ?)",
            ("1","adnan","adnan123")

)
           

connection.commit()
connection.close()