#Написать модуль, содержащий 12 функци по
#переводу:

#DUIMES - SM
def d_s(a):
    s = a * 2.54
    return f"{a} Дюймов = {round(s,2)} сантиметров \n"

#SM - DUIMES
def s_d(a):
    s = a / 2.54
    return f"{a} Сантиметров = {round(s,2)} Дюймов \n"

#MIles - KIlometers
def m_k(a):
    s = a * 1.609
    return f"{a} Миль = {round(s,2)} Километров \n"

#KIlometers - MIles
def k_m(a):
    s = a / 1.609
    return f"{a} Километров = {round(s, 2)} Миль \n"


#Funts - Kilograms
def f_k(a):
    s = a * 0.453592
    return f"{a} Фунтов = {round(s, 2)} Килограм \n"


#Kilograms - Funts
def k_f(a):
    s = a * 2.20462
    return f"{a} Килограм = {round(s, 2)} Фунтов \n"

#Unci - Gram
def y_g(a):
    s = a * 28.3495
    return f"{a} Унций = {round(s, 2)} Грамм \n"


#Gram - Unci
def g_y(a):
    s = a / 28.3495
    return f"{a} Грамм = {round(s, 2)} Унций \n"


#Gallons - Litres
def g_l(a):
    s = a * 3.785
    return f"{a} Галлон = {round(s, 2)} Литров \n"


#Litres - Gallons
def l_g(a):
    s = a / 3.785
    return f"{a} Литров = {round(s, 2)} Галлон \n"


#Pinta - Litres
def p_l(a):
    s = a * 0.568261
    return f"{a} Пинты = {round(s, 2)} Литров \n"

#Litres - Pinta
def l_p(a):
    s = a * 1.75975
    return f"{a} Литров = {round(s, 2)} Пинты \n"

def main():
    while True:
        print(f"1 - Дюймы в сантиметры")
        print(f"2 - Сантиметры в дюймы")
        print(f"3 - Мили в километры")
        print(f"4 - Километры в мили")
        print(f"5 - Фунты в килограмы")
        print(f"6 - Килограмы в фунты")
        print(f"7 - Унции в граммы")
        print(f"8 - Граммы в унции")
        print(f"9 - Галлон в литры")
        print(f"10 - Литры в галлоны")
        print(f"11 - Пинты в литры")
        print(f"12 - Литры в пинты")
        print(f"0 - Закрыть программу")
        answer = input("Выберите нужный вам вариант: \n")
        if not answer.isdigit():
            print(f"Вы ввели букву! А нужно число!\n")
            continue
        if answer == '1':
            print(f"Вы выбрали Дюймы в Сантиметры")
            a = int(input("Введите длинну в дюймах: \n" ))
            print(d_s(a))
        elif answer == '2':
            print(f"Вы выбрали Сантиметры в Дюймы")
            a = int(input("Введите длинну в Сантиметрах: \n" ))
            print(s_d(a))
        elif answer == '3':
            print(f"Вы выбрали Мили в Километры")
            a = int(input("Введите длинну в Милях: \n" ))
            print(m_k(a))
        elif answer == '4':
            print(f"Вы выбрали Километры в Милях")
            a = int(input("Введите длинну в Километрах: \n" ))
            print(k_m(a))
        elif answer == '5':
            print(f"Вы выбрали Фунты в Килограмы")
            a = int(input("Введите вес в Фунтах: \n" ))
            print(f_k(a))
        elif answer == '6':
            print(f"Вы выбрали Килограмы в Фунты")
            a = int(input("Введите вес в Килограмах: \n" ))
            print(k_f(a))
        elif answer == '7':
            print(f"Вы выбрали Унции в Граммы")
            a = int(input("Введите вес в Унциях: \n" ))
            print(y_g(a))
        elif answer == '8':
            print(f"Вы выбрали Граммы в Унции")
            a = int(input("Введите вес в Граммах: \n" ))
            print(g_y(a))
        elif answer == '9':
            print(f"Вы выбрали Галлон в Литры")
            a = int(input("Введите объем в Галлонах: \n" ))
            print(g_l(a))
        elif answer == '10':
            print(f"Вы выбрали Литры в Галлоны")
            a = int(input("Введите объем в Литрах: \n" ))
            print(l_g(a))
        elif answer == '11':
            print(f"Вы выбрали Пинты в Литры")
            a = int(input("Введите объем в Пинтах: \n" ))
            print(p_l(a))
        elif answer == '12':
            print(f"Вы выбрали Литры в Пинты")
            a = int(input("Введите объем в Литрах: \n" ))
            print(l_p(a))
        elif answer == '0':
            print(f"Всего доброго!")
            break
        else:
            print(f"Введите правильный вариант!!!!")
            continue
if __name__ == '__main__':
    print(f"Добро пожаловать в конвертер! \n")
    main()
