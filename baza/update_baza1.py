import sqlite3

con = sqlite3.connect('baze1.db')

def sql_update(con):

    cursorObj = con.cursor()

    cursorObj.execute('UPDATE employees SET second = "Petrov" where id = 3')

    con.commit()

sql_update(con)
