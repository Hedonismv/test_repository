import psycopg2

try:
    conn = psycopg2.connect(dbname='gui', user='postgres', password='123', host='localhost')  # db authorization
    cursor = conn.cursor()
    print('Подключение прошло успешно')
except ConnectionError:
    print('Не удалось подключиться к базе данных')


def add_the_car(*car_info):
    try:
        cursor.execute("INSERT INTO "
                       "car (brand_id, car_model, car_release_year)"
                       " VALUES (%s, %s, %s);", car_info)
        conn.commit()
        print('Машина успешно добавлена в базу данных')
    except Exception as e:
        print(F'Error {e} occurred')


def add_the_brand(name):
    try:
        cursor.execute("INSERT INTO "
                       "brand (brand_name)"
                       " VALUES(%s);", name)
        conn.commit()
        print('Бренд успешно добавлен в базу данных')
    except Exception as e:
        print(F'Error {e} occurred')


def read_the_car():
    cursor.execute("SELECT brand_name, car_model, car_release_year FROM brand"
                   " INNER JOIN gui.public.car ON brand.brand_id = car.brand_id ")
    car_list = cursor.fetchall()
    for brand_name, car_model, car_release_year in car_list:
        print(  # f'\nID Продукта - {p_id}\n'
            f'***********************************\n'
            f'Название Бренда - {brand_name}\n'
            f'Модель автомобиля - {car_model}\n'
            f'Год выпуска - {car_release_year}\n'
            f'***********************************\n')
    conn.commit()


def read_the_brand():
    cursor.execute("SELECT * FROM brand")
    brand_list = cursor.fetchall()
    for brand_id, brand_name in brand_list:
        print(  # f'\nID Продукта - {p_id}\n'
            f'***********************************\n'
            f'ID Бренда - {brand_id}'
            f'Название Бренда - {brand_name}\n'
            f'***********************************\n')
    conn.commit()


def update_the_car(c_id, car_m_name):
    cur.execute(f"""UPDATE car SET car_model = {car_m_name} WHERE car_id = {c_id} """)
    conn.commit()
    print('Модель авто заменена')


def update_the_brand(b_id, b_name):
    cur.execute(f"""UPDATE brand SET brand_name = {b_name} WHERE brand_id = {b_id} """)
    conn.commit()
    print('Название бренда заменено')


def delete_the_car(c_id):
    cur.execute(f"""DELETE FROM car WHERE gui.public.car.car_id = {c_id}""")
    conn.commit()
    print('Авто удалено')


def delete_the_brand(b_id):
    cur.execute(f"""DELETE FROM brand WHERE brand_id = {b_id}""")
    conn.commit()
    print('Бренд удален')
# cursor.execute("""CREATE TABLE IF NOT EXISTS brand(
#     brand_id SERIAL PRIMARY KEY ,
#     brand_name TEXT NOT NULL UNIQUE);
# """)
# conn.commit()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS car(
#     car_id SERIAL PRIMARY KEY ,
#     brand_id INTEGER,
#     car_model TEXT NOT NULL ,
#     car_release_year INTEGER NOT NULL ,
#     CONSTRAINT fk_brand
#         FOREIGN KEY (brand_id)
#             REFERENCES brand(brand_id)
#                 ON DELETE CASCADE );
# """)
# conn.commit()
