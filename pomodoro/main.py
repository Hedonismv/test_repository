# Создать программу Pomodoro ( https://ru.wikipedia.org/wiki/
# Метод_помидора ).
# На вход программа получает имя, фамилию, время для
# фокусировки(по-умолчанию 25 минут), длину перерыва(по-
# умолчанию 5 минут), количество циклов(по-умолчанию 4) и
# название задачи. Программа указывает оставшееся время
# фокусировки, после сигнализирует о наступлении перерыва,
# после сигнализирует о начале нового цикла фокусировки.
# Программа должна вести фа л лога о всех запусках.

from user import User
from time_exceptions import *


def main():
    name = input('Введите ваше имя:')  # Take a name
    surname = input('Введите вашу фамилию:')  # Take a surname
    task = input('Введите название задачи')  # Take a Task name
    usr = User(name, surname, task)  # init a class USER
    print(usr)  # call repr magic method
    usr.init_user()  # append user to LOG
    except_time()


if __name__ == '__main__':
    main()
