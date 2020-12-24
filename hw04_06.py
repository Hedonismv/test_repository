#Введите число. Если это число делиться на 1000 без
#остатка, то выведите на экран "millennium".

def millennium():
    number = int(input("Введите число: "))
    if number %1000 == 0:
        print("millennium")
    else:
        print("NOT millennium")


if __name__ == '__main__':
    millennium()
