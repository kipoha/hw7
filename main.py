import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def add_product(connection, product):
    sql = '''INSERT INTO products 
    (product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def add_quantity(connection, quantity):
    sql = '''UPDATE products SET quantity = quantity + ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, quantity)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_price(connection, price):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, price)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def remove_products(connection, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def show_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()
        print('Полный список продуктов')
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def show_products_with_limit(connection, price_limit, quantity_limit):
    sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows_list = cursor.fetchall()
        print('\nПродукты с лимитом')
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def show_products_with_name(connection, name):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (name, ))
        rows_list = cursor.fetchall()
        print('\nПродукты по названию')
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


products = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)'''


connect = create_connection('hw.db')
if connect is not None:
    print("Done!")
    # create_table(connect, products)
    # add_product(connect, ('Карамельный попкорн', 60.5, 30))
    # add_product(connect, ('Классический попкорн', 55.5, 25))
    # add_product(connect, ('Чипсы со вкусом сыра', 86.5, 60))
    # add_product(connect, ('Чипсы со вкусом зелени', 86.5, 70))
    # add_product(connect, ('Обычное мыло', 64.5, 5))
    # add_product(connect, ('49% хоз. мыло', 70, 4))
    # add_product(connect, ('Торт Бархат', 99.5, 16))
    # add_product(connect, ('Торт Сникерс', 99.5, 15))
    # add_product(connect, ('Кухонный нож', 700, 5))
    # add_product(connect, ('Охотничий нож', 1300, 5))
    # add_product(connect, ('Диск с игрой', 500.5, 30))
    # add_product(connect, ('Музыкальный диск', 450.5, 30))
    # add_product(connect, ('Механическая клавиатура', 4200.5, 30))
    # add_product(connect, ('Мембраная клавиатура', 1200.5, 30))
    # add_product(connect, ('Оптическая клавиатура', 3000.5, 30))
    # add_quantity(connect, (10, 6))
    # update_price(connect, (550, 11))
    # remove_products(connect, 4)
    show_products(connect)
    show_products_with_limit(connect, 100, 5)
    show_products_with_name(connect, '%клавиатура%')
