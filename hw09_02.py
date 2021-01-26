#Создать класс Car. Атрибуты: марка, модель, год
#выпуска, скорость(по умолчанию 0). Методы:
#увеличить скорости(скорость + 5), уменьшение
#скорости(скорость - 5), стоп(сброс скорости на 0),
#отображение скорости, разворот(изменение знака
#скорости). Все атрибуты приватные.

class Car():
    """docstring for Car."""

    def __init__(self, mark, model, year, speed = 0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speed_up(self):
        self.__speed += 5

    def speed_down(self):
        if self.__speed - 5 < 0:
            print('Скорость не может быть ниже нуля')
        else:
            self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def display_speed(self):
        print('Скорость : {} км/ч'.format(self.__speed))

    def display_info(self):
        print('Автомобиль {} {}\nГод выпуска - {}\nСкорость : {} км/ч'.format(self.__mark, self.__model, self.__year, self.__speed))

mercedes = Car('Mercedes', 'E220', '2019')
mercedes.speed_up()
mercedes.speed_down()
mercedes.speed_down()
mercedes.display_speed()
mercedes.display_info()
