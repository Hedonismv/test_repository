#Создать три класса, описывающие реальные объекты.
#Кажды класс должен содержать минимум три
#приватных атрибута, конструктор, геттеры и сеттеры
#для каждого атрибута, два метода.


class Dog():
    def __init__(self, name, breed, sex, age=1):
        self.__name = name
        self.__breed = breed
        self.__sex = sex
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Ну не может ей быть столько')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.isalpha():
            return self.__name
        else:
            print('Некорректно введно имя')

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if sex.isalpha():
            print('Быть такого не может')
        else:
            return self.__sex

    def breed(self):
        return self.__breed

    def display_info(self):
        print('Имя-{}\nПорода-{}\nПол-{}\nЛет-{}'.format(self.__name, self.__breed, self.__sex, self.__age))

    def woof(self):
        print('WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOF')

mike = Dog('Mike','haski','m')
mike.age = -12
mike.age = 4
mike.display_info()
mike.woof()

class HockeyPlayer():
    def __init__(self, name, number, xLocation=0, yLocation=0):
        self.__name = name
        self.__number = number
        self.__xLocation = 0
        self.__yLocation = 0

    def run_left(self):
         self.__yLocation -= 10

    def run_right(self):
         self.__yLocation += 10

    def run_up(self):
         self.__xLocation += 10

    def run_down(self):
         self.__xLocation -= 10

    def display_coord(self):
        print('X:{} Y:{}'.format(self.__xLocation, self.__yLocation))

    def display_info(self):
        print('Name: {}\nNumber: {}\nX:{} Y:{}'.format(self.__name, self.__number, self.__xLocation, self.__yLocation))

h = HockeyPlayer('David','14')
h.run_up()
h.run_left()
h.run_left()
h.display_info()

class Distance():
    def __init__(self):

        self._distance = 0.0

    @property
    def in_metres(self):
        return self._distance

    @in_metres.setter
    def in_metres(self, val):
        try:
            self._distance = float(val)
        except:
            raise ValueError("Need num")

    @property
    def in_feet(self):
        return self._distance * 3.2808399

    @in_feet.setter
    def in_feet(self, val):
        try:
            self._distance = float(val) / 3.2808399
        except:
            raise ValueError("Need num")

    @property
    def in_parsecs(self):
        return self._distance * 3.24078e-17

    @in_parsecs.setter
    def in_parsecs(self, val):
        try:
            self._distance = float(val) / 3.24078e-17
        except:
            raise ValueError("Need num")
distance = Distance()
distance.in_metres = 1000.0
