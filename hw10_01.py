#Создать класс MyTime. Атрибуты: hours, minutes,
#seconds. Методы: переопределить магические методы
#сравнения(==, !=, >=, <=, <, >), сложения, вычитания,
#умножения на число, вывод на экран.
#Примечание: список «магических методов» можно
#посмотреть тут: https://pythonworld.ru/osnovy/
#peregruzka-operatorov.html
from datetime import datetime, date, time

class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def take_date():
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    def __repr__(self):
        return f"date and time =, {dt_string}"

    def __eq__(self):
        """ == """
        pass

    def __ne__(self):
        """ != """
        pass

    def __ge__(self):
        """ >= """
        pass

    def __le__(self):
        """ >= """
        pass

    def __lt__(self):
        """ < """
        pass

    def __gt__(self):
        """ > """
        pass

    def __add__(self):
        """ + """
        pass

    def __sub__(self):
        """ - """
        pass

    def __mul__(self):
        """ * """
        pass


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print()
