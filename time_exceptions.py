from timer import Timer

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
        hours = int(input('Введите Часы:'))
        if hours > 24:
            raise HourException
    except HourException as h:
        print(h)
    while hours > 24:
        try:
            hours = int(input('Введите Часы:'))
            if hours > 24:
                raise HourException
        except ValueError as h:
            print(h)
            ################
    else:
        try:
            minutes = int(input('Введите Минуты:'))
            if minutes > 60:
                raise MinuteException
        except MinuteException as m:
            print(m)
        while minutes > 60:
            try:
                minutes = int(input('Введите Минуты:'))
                if minutes > 60:
                    raise MinuteException
            except MinuteException as m:
                print(m)
                #################
        else:
            try:
                seconds = int(input('Введите Секунды:'))
                if seconds > 60:
                    raise SecondException
            except SecondException as s:
                print(s)
            while seconds > 60:
                try:
                    seconds = int(input('Введите Секунды:'))
                    if seconds > 60:
                        raise SecondException
                except SecondException as s:
                    print(s)
                    #####################
            else:
                tm = Timer(hours, minutes, seconds)
                #print(tm)
                tm.start_timer()
