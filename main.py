# Создать таблицы Brand(name), Car(model, release_year,
# brand(foreign key на таблицу Brand)). Реализовать
# CRUD(создание, чтение, обновление по id, удаление
# по id) для бренда и машины. Создать
# пользовательский интерфейс (использовать
# разделение логики по модулям - ui отдельно, работа с
# БД отдельно, запуск программы из консоли отдельно и
# т.д. в зависимости от логики приложения).
from database.db import *


def main():
    user_choice = None
    while user_choice != 0:
        user_choice = int(input('Число в соответствии с пунктом: '))
        if user_choice == 1:
            b_id = int(input('ID - Бренда'))
            c_model = input('Модель автомобиля')
            c_r_year = input('Год выпуска')
            add_the_car(b_id, c_model, c_r_year)
        elif user_choice == 2:
            read_the_car()
        elif user_choice == 3:
            c_id = int(input('ID - Авто'))
            c_m_name = input('Название модели')
            update_the_car(c_id, c_m_name)
        elif user_choice == 4:
            c_id = int(input('ID - Авто'))
            delete_the_car(c_id)
        elif user_choice == 5:
            print('Для начала рекоммендуется выбрать 2, чтобы просмотреть\n'
                  'Все данные базы данных, потом уже удалять,\n'
                  'меня названия и тд, если она пустая, то добавьте\n'
                  'туда товары, но помните что названия должны быть уникальны.\n')
        elif user_choice == 0:
            print(f'Всего доброго')
            break
        else:
            print('Что то пошло не так')


if __name__ == '__main__':
    print('Выберите нужный вам вариант:\n'
          '1. Создание\n'
          '2. Чтение\n'
          '3. Модификация\n'
          '4. Удаление\n'
          '5. Информация\n'
          'Выход - Введите 0')
    main()
