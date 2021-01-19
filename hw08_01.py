#Создать декоратор для функции, которая принимает
#список чисел. Декоратор должен производить
#предварительную проверку данных - удалять все
#четные элементы из списка.
def f_decorator(func):
    """Декоратор """
    def filter(numbers:list) -> list:
        """Функция декоратора, которая проверяет список на наличие четных
        элементов и удаляет их из списка """
        copy = numbers.copy()
        copy.clear()
        for n in numbers:
            if n % 2 == 0:
                continue
            else:
                copy.append(n)
        print(copy)
    return filter

@f_decorator
def args(numbers:list) -> list:
    """принимает список и выводит его"""
    print(numbers)


n_list = [3,4,5,6,3,2,8,9,5,3]

args(n_list)
