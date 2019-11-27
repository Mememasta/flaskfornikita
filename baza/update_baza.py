import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_update(con):

    cursorObj = con.cursor()

    cursorObj.execute('UPDATE employees SET salary = 4567 where id = 5')

    con.commit()

sql_update(con)
