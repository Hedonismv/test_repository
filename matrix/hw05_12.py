#2. Создать две новые матрицы matrix_a, matrix_b
#случа ных чисел размерностью n*m;
#. создать матрицу равную сумме matrix_a и matrix_b;
#b.
#создать матрицу равную разности matrix_a и
#matrix_b;
#c. создать новую матрицу равную matrix_a умноженно
#на число g. g вводится с клавиатуры.
import numpy as np
from random import randint


#START THE FUNCTION
dig = 0
nums = []
nums1 = []
nums2 = []
n = int(input("Введите размерность  матрицы: "))
m = int(input("Введите размерность  матрицы: "))
a = int(input("От: "))
b = int(input("До: "))
g = int(input("На сколько умножим: "))
matrix_a = np.array([[randint(a,b) for y in range(n)] for x in range (m)])
matrix_b = np.array([[randint(a,b) for y in range(n)] for x in range (m)])
for xy in range(n):
    print(matrix_a[xy])
print()
for xy in range(n):
    print(matrix_b[xy])

print()
summ = matrix_a + matrix_b
des = matrix_a / matrix_b
multy = matrix_a * g

print(summ)
print()
print(des)
print()
print(multy)
