#Составить список чисел Фибоначчи содержащи 15
#элементов.
#(подсказка: числа Фибоначчи - последовательность, в
#которо первые два числа равны либо 1 и 1, а каждое
#последующее число равно сумме двух предыдущих
#чисел. Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )

fib1 = fib2 = 1
fib_list = []
fib_list.append(fib1)
fib_list.append(fib2)

n = int(input("Введите количество элементов: "))

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
