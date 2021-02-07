# Создать таблицу продуктов. Атрибуты продукта: id,
# название, цена, количество, комментарий. Реализовать
# CRUD(создание, чтение, обновление по id, удаление
# по id) для продуктов. Создать пользовательский
# интерфейс(использовать разделение логики по
# модулям - ui отдельно, работа с БД отдельно, запуск
# программы из консоли отдельно и т.д. в зависимости от
# логики приложения).
from database.db import add_the_product, read_the_product, update_the_product, delete_the_product


def main():
    user_choice = None
    while user_choice != 0:
        user_choice = int(input('Число в соответствии с пунктом: '))
        if user_choice == 1:
            name = input('Название товара: ')
            price = input('Цена товара: ')
            num = input('Количество товара: ')
            com = input('Комментарий товара: ')
            add_the_product(name, price, num, com)
        elif user_choice == 2:
            read_the_product()
        elif user_choice == 3:
            p_id = int(input('Введите id товара, где вы хотите заменить название: '))
            p_name = input('Введите новое название товара: ')
            update_the_product(p_id, p_name)
        elif user_choice == 4:
            p_id = int(input('Введите id товара, который вы хотите удалить: '))
            delete_the_product(p_id)
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
