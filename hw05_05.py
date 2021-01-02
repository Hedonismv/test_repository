#В списке целых случайных чисел с количеством
#элементов n определить максимальное число и
#заменить им все четные по значению элементы.
from random import randint

def main():
    n = int(input("Введите количество элементов: "))
    a = int(input("От: "))
    b = int(input("До: "))
    r_list = [randint(a,b) for i in range(n)]
    max_num = max(r_list)
    print(f"Сгенерировали список: {r_list}")
    print(f"Максимальное число в списке: {max_num}")
    for i in r_list:
        if i % 2 == 0:
            r_list.remove(i)
            r_list.append(max_num)
    print(f"Готовый список: {r_list}")
if __name__ == '__main__':
    main()
