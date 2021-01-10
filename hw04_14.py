#Составить список чисел Фибоначчи содержащи 15
#элементов.
#(подсказка: числа Фибоначчи - последовательность, в
#которо первые два числа равны либо 1 и 1, а каждое
#последующее число равно сумме двух предыдущих
#чисел. Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
def main():
    fib1 = fib2 = 1
    fib_list = []
    fib_list.append(fib1)
    fib_list.append(fib2)

    n = int(input("FOR Method Введите количество элементов: "))

    if n < 2:
        quit()

    print(fib1, end=' ')
    print(fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib2)
        print(fib2, end=' ')
    print(f"\n{fib_list}")
    print()

def second():
    fib1 = fib2 = 1
    fib_list = []
    fib_list.append(fib1)
    fib_list.append(fib2)
    i = 0
    v = 1

    n = int(input("WHILE Method Введите количество элементов: "))

    if n < 2:
        quit()

    while i < n - 2:
        #print(fib_list)
        num = fib_list[i] + fib_list[v]
        #print(f"{i} I --- {v} V")    # DEBUG:
        #print(f"{num} NUM")
        fib_list.append(num)
        i += 1
        v += 1
        continue
    print(fib_list)



if __name__ == '__main__':
    main()
    second()
