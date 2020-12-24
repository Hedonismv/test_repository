#В семье N свадьба. Они решили выбрать заведение,
#где будут праздновать в зависимости от количества
#людей , которое прибудет к утру.
#Если их будет больше 50 - закажут ресторан, если от
#20 до 50 -то кафе, а если меньше 20 то отпраздную
#дома.
#Вывести "ресторан", "кафе", "дом" в зависимости от
#количества гостей.

def wedding():
    peoples = int(input("Введите количество гостей: "))

    if peoples > 50:
        print(f"Будет {peoples} человека, поэтому закажем ресторан")
    elif peoples >= 20 and peoples <= 50:
        print(f"Будет {peoples} человека, поэтому пойдем в кафе")
    elif peoples < 20:
        print(f"Будет {peoples} человека, поэтому отпразднуем дома")
    else:
        print(f"Что то пошло не так, введите число")

if __name__ == '__main__':
    wedding()
