#Написать программу та мер. Программа при запуске
#принимает имя, фамилию, часы, минуты и секунды.
#После программа начинает обратны отсчет выводя
#оставшееся время. Программа должна хранить фа л
#логирования с информацие о том кто запускал
#программу и когда.
from user import User
from time_exceptions import *

def main():
    name = input('Введите ваше имя:')  # Take a name
    surname = input('Введите вашу фамилию:') # Take a surname
    usr = User(name, surname)  # INit a class USER
    print(usr) # call repr dunder method
    usr.init_user() # append user to LOg
    except_time()  # call time_exceptions FUNC

if __name__ == '__main__':
    main()
