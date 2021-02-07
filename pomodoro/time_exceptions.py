from time_pomodoro import Pomodoro


class HourException(Exception):
    def __init__(self, message='Значение часов не может быть больше 24!'):
        super().__init__(message)


class MinuteException(Exception):
    def __init__(self, message='Значение минут не может быть больше 60!'):
        super().__init__(message)


class SecondException(Exception):
    def __init__(self, message='Значение секунд не может быть больше 60!'):
        super().__init__(message)


def except_time():
    """ Функция , которая прнимает переменные hours,minutes,seconds
, переменные проверяются и передаются в класс Timer, где идет основной процесс
над значениями
    """
    try:
        f_time = int(input('Введите время для фокусировки:'))
        if f_time > 60:
            raise HourException
    except HourException as h:
        print(h)
    while f_time > 60:
        try:
            f_time = int(input('Введите время для фокусировки:'))
            if f_time > 24:
                raise HourException
        except ValueError as h:
            print(h)
            ################
    else:
        try:
            b_time = int(input('Введите длинну перерыва:'))
            if b_time > 60:
                raise MinuteException
        except MinuteException as m:
            print(m)
        while b_time > 60:
            try:
                b_time = int(input('Введите длинну перерыва:'))
                if b_time > 60:
                    raise MinuteException
            except MinuteException as m:
                print(m)
                #################
        else:
            try:
                cycles = int(input('Введите кол-во циклов:'))
                if cycles > 10:
                    raise SecondException
            except SecondException as s:
                print(s)
            while cycles > 10:
                try:
                    cycles = int(input('Введите кол-во циклов:'))
                    if cycles > 60:
                        raise SecondException
                except SecondException as s:
                    print(s)
                    #####################
            else:
                tm = Pomodoro(f_time, b_time, cycles)
                # print(tm)
                tm.pomodoro_func()
