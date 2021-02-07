import sqlite3

conn = sqlite3.connect('test.db')  # db authorization
cur = conn.cursor()  # take a cursor from DB

cur.execute("""CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL UNIQUE ,
    product_price INTEGER NOT NULL ,
    product_num INTEGER  NOT NULL,
    product_com TEXT NOT NULL);
""")
conn.commit()


def add_the_product(*product):
    try:
        cur.execute("INSERT INTO "
                    "products (product_name, product_price, product_num, product_com)"
                    " VALUES(?, ?, ?, ?);", product)
        conn.commit()
        print('Продукт успешно добавлен в базу данных')
    except Exception as e:
        print(F'Error {e} occurred')


def read_the_product():
    cur.execute("SELECT * FROM products;")
    prod_list = cur.fetchall()
    for p_id, p_name, p_price, p_num, p_com in prod_list:
        print(f'\nID Продукта - {p_id}\n'
              f'Название продукта - {p_name}\n'
              f'Цена продукта - {p_price} BYN\n'
              f'Количество на складе - {p_num}\n'
              f'Комментарий по продукту - {p_com}\n'
              f'***********************************\n')


def update_the_product(p_id, p_name):
    cur.execute(f"""UPDATE products SET product_name = "{p_name}" WHERE product_id = {p_id} """)
    conn.commit()
    print('Название продукта заменено')


def delete_the_product(p_id):
    cur.execute(f"""DELETE FROM products WHERE product_id = {p_id}""")
    conn.commit()
    print('Товар успешно удален')
