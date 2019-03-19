import sqlite3


def create_table():
    connection = sqlite3.connect('lite.db')     # connection with new or existing SQLite db
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)')       # REAL/float

    connection.commit()
    connection.close()


def insert(item, quantity, price):
    connection = sqlite3.connect('lite.db')     # connection with new or existing SQLite db
    cursor = connection.cursor()
    # cursor.execute('INSERT INTO store VALUES (\'Kitkat\', 50, 0.80)')
    sql_string = f'INSERT INTO store VALUES (\'{item}\', {quantity},{price})'
    # print(sql_string)
    cursor.execute(sql_string)    # NB f prefix
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect('lite.db')     # connection with new or existing SQLite db
    cursor = connection.cursor()
    sql_string = f'SELECT * FROM store'
    # print(sql_string)
    cursor.execute(sql_string)    # NB f prefix
    rows = cursor.fetchall()
    connection.close()
    return rows                 # return fetched data


print(view())
# insert('Marathon',100, 0.75)
