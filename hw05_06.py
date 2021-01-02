#Задан целочисленны список c n случайных
#элементов. Определить количество участков списка,
#на котором элементы монотонно возрастают (каждое
#следующее число больше предыдущего).
from random import randint
from itertools import groupby

def main():
    n = randint(1,20)
    a = int(input("От: "))
    b = int(input("До: "))
    r_list = [randint(a,b) for _ in range(n)]
    scale = ''
    print(f"Сгенерировали список: {r_list}")
    count = 0
    lenght = len(r_list)
    for i in range(1, lenght):
        if r_list[i-1] < r_list[i]: scale += '+'
        else: scale += '-'
    group = groupby(scale)
    result = [k for k,v in group if k == '+']

    print('Количество участков:', len(result))
if __name__ == '__main__':
    main()
