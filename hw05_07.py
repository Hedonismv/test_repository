#Дана целочисленная квадратная матрица размерности
#n. Заполнить ее случайными целыми числами. На ти в
#каждо строке наибольши элемент и поменять его
#местами с элементом главно диагонали.
from random import randint

def print_matrix(matrix):
    for row in matrix:
        new_row = str(row)
        new_row = new_row.replace(',','')
        new_row = new_row.replace('[','')
        new_row = new_row.replace(']','')
        print(new_row)
        ### any
        max_num = max(test_matrix[xy])
        print(max_num)
        print(f"DIG: {dig}")
        dig += 1
        print(f"DIG: {dig}")
        print(test_matrix[xy])
dig = 0
n = int(input("Введите размерность квадратной матрицы: "))
test_matrix = [[randint(10,99) for y in range(n)] for x in range (n)]
for xy in range(n):
    print(test_matrix[xy])
for c in test_matrix:
    print(f"new {c}")
for c in test_matrix:
    #print(f"new {c}")
    max_num = max(c)
    ind = c.index(max_num,0,5)
    #print(f"INDEX: {ind}")
    #print(f"MAX: {max_num}")
    if c[dig] != max_num:
        c[dig], c[ind] = c[ind], c[dig]
        #print(f"EXECUTED: {c}")
    #print(f"MAIN DEO: {c[dig]}")
    dig += 1
    print(f"MAIN: {c}")
