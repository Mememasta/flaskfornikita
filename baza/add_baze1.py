import sqlite3

con = sqlite3.connect('baze1.db')

def sql_insert(con, entities):

    cursorObj = con.cursor()

    cursorObj.execute('INSERT INTO employees(id, name, second, photo) VALUES(?, ?, ?, ?)', entities)

    con.commit()

entities = (6, 'Petr',  'Trushko', 'No')

sql_insert(con, entities)
