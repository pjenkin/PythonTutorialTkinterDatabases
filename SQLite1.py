import sqlite3


def with_connection(func):
    # https://www.udemy.com/the-python-mega-course/learn/v4/questions/6470378
    # using custom decorator function, to abbreviate connection/disconnection code
    def wrapper(*args, **kwargs):
        global connection
        connection = sqlite3.connect('lite.db')
        global cursor
        cursor = connection.cursor()
        return func(*args, **kwargs)    # https://realpython.com/inner-functions-what-are-they-good-for/
        del cursor        # del for deleting objects
        del connection
    return wrapper
# https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3#understanding-**kwargs
# "**kwargs allows you to pass keyworded variable length of arguments to a function.
# You should use **kwargs if you want to handle named arguments in a function."
# *args is used to send a non-keyworded variable length argument list to the function

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


# def update(item, quantity, price):
#     connection = sqlite3.connect('lite.db')     # connection with new or existing SQLite db
#     cursor = connection.cursor()
#     # sql_string = f'DELETE FROM store WHERE item=\'{item}\'' # NB f prefix
#     sql_string = f'UPDATE store SET quantity={quantity}, price={price} WHERE item=\'{item}\'' # NB f prefix
#     print(sql_string)
#     cursor.execute(sql_string)    # NB f prefix
#     # cursor.execute('DELETE FROM store WHERE item=?', (item,))     # no comma needed at end if >1 parameter (item1, item2)
#     connection.commit()
#     connection.close()

# abbreviated version of 'update' below, using custom decorator

@with_connection
def update(item, quantity, price):
    sql_string = f'UPDATE store SET quantity={quantity}, price={price} WHERE item=\'{item}\'' # NB f prefix
    print(sql_string)
    cursor.execute(sql_string)    # NB f prefix
    connection.commit()


@with_connection
def update_kwargs(**some_kwargs):       # kwargs not mandatory, the ** is important though
    # https://www.udemy.com/the-python-mega-course/learn/v4/questions/4934682
    #sql_string = f'UPDATE store SET quantity={quantity}, price={price} WHERE item=\'{item}\'' # NB f prefix
    #sql_string = f'UPDATE store SET quantity={some_kwargs["quantity"]}, price={some_kwargs["price"]} WHERE item=\'{some_kwargs["item"]}\'' # NB f prefix
    sql_string = f'UPDATE store SET quantity={some_kwargs.get("quantity", 1)}, price={some_kwargs.get("price",1)} WHERE item=\'{some_kwargs["item"]}\'' # NB f prefix
    # could have conditional to omit parameters from SQL, perhaps, if values absent from function call arguments
    print(sql_string)
    cursor.execute(sql_string)    # NB f prefix
    connection.commit()


#insert('Kitkat', 100, 0.75)
update('Kitkat', 100, 0.5, )
print(view())
insert('Marathon', 100, 0.75)
print(view())
delete('Marathon')
print(view())
update('Kitkat', 200, 0.5 )
print(view())
update_kwargs(item='Kitkat',quantity=300, price=0.40)
print(view())
update_kwargs(item='Kitkat')
print(view())
