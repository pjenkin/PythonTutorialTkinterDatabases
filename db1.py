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

def delete(item):
    connection = sqlite3.connect('lite.db')     # connection with new or existing SQLite db
    cursor = connection.cursor()
    # sql_string = f'DELETE FROM store WHERE item=\'{item}\'' # NB f prefix
    sql_string = f'DELETE FROM store WHERE item=\'{item}\'' # NB f prefix
    print(sql_string)
    cursor.execute(sql_string)    # NB f prefix
    # cursor.execute('DELETE FROM store WHERE item=?', (item,))
    connection.commit()
    connection.close()


def update(item, quantity, price):
    connection = sqlite3.connect('lite.db')     # connection with new or existing SQLite db
    cursor = connection.cursor()
    # sql_string = f'DELETE FROM store WHERE item=\'{item}\'' # NB f prefix
    sql_string = f'UPDATE store SET quantity={quantity}, price={price} WHERE item=\'{item}\'' # NB f prefix
    print(sql_string)
    cursor.execute(sql_string)    # NB f prefix
    # cursor.execute('DELETE FROM store WHERE item=?', (item,))     # no comma needed at end if >1 parameter (item1, item2)
    connection.commit()
    connection.close()

#insert('Kitkat', 100, 0.75)
update('Kitkat', 100, 0.5, )
print(view())
insert('Marathon', 100, 0.75)
print(view())
delete('Marathon')
print(view())
update('Kitkat', 200, 0.5, )
print(view())
