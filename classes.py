#Создать класс Point, описывающи точку(атрибуты: x,
#y). Создать класс Figure. Создать три дочерних класса
#Circle(атрибуты: координаты центра(тип Point), радиус;
#методы: нахождение периметра и площади
#окружности), Triangle(атрибуты: три точки, методы:
#нахождение площади и периметра), Square(атрибуты:
#две точки, методы: нахождение площади и
#периметра). При необходимости, создавать все
#необходимые методы, не описанные в задании.
#Создать список фигур и в цикле подсчитать и вывести
#площади всех фигур на экран в формате: «Тип
#фигуры» -> «площадь».
#Примечание: в рамках задания создать два фа ла:
#classes.py и main.py. В первом будут описаны все
#классы, во втором классы будут импортированы и
#использованы.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figure:
    pass

class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        result_p = self.radius * (3.14 * 2)
        return result_p

    def square(self):
        result_s = 3.14 * (self.radius ** 2)
        return result_s

    def __repr__(self):
        return f"Круг. Периметр  - . Площадь - "

class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        result_p = self.a + self.b + self.c
        return result_p

    def square(self):
        result_s = (self.a * self.b) / 2
        return result_s

    def __repr__(self):
        return f"Треугольник. Периметр - . Площадь - "


class Square(Figure):

    def __init__(self, a, b):
        pass

    def perimeter():
        pass

    def square():
        pass
