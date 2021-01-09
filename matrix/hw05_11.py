#1. Создать матрицу случа ных чисел от a до b,
#размерность матрицы n*m;
#a. на ти максимальны элемент матрицы;
#b. на ти минимальны минимальны матрицы;
#c. на ти сумму всех элементов матрицы;
#d. на ти индекс ряда с максимально суммо
#элементов;
#e. на ти индекс колонки с максимально суммо
#элементов;
#f.на ти индекс ряда с минимально суммо
#элементов;
#g. на ти индекс колонки с минимально суммо
#элементов;
#h. обнулить все элементы выше главно диагонали;
#i.обнулить все элементы ниже главно диагонали.

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
test_matrix = [[randint(a,b) for y in range(n)] for x in range (m)]
for xy in range(n):
    print(test_matrix[xy])
#MAX ELEMENT
for c in test_matrix:
    max_num = max(c)
    nums.append(max_num)
max_main = max(nums)
print(f"Максимальный элемент - {max_main}")
nums.clear()
#MIN ELEMENT
for c in test_matrix:
    min_num = min(c)
    nums.append(min_num)
min_main = min(nums)
print(f"Минимальный элемент - {min_main}")
nums.clear()
#SUMM
for c in test_matrix:
    summa = sum(c)
    nums.append(summa)
summa_main = sum(nums)
print(f"Сумма - {summa_main}")
nums.clear()
#INDEX MAX R
for c in test_matrix:
    summa = sum(c)
    nums.append(summa)
max_main = max(nums)
r_index = nums.index(max_main,0,b)
print(f"Индекс максимального ряда - {r_index}")
nums.clear()
#INDEX MIN R
for c in test_matrix:
    summa = sum(c)
    nums.append(summa)
min_main = min(nums)
r_index = nums.index(min_main,0,b)
print(f"Индекс минимального ряда - {r_index}")
nums.clear()
#INDEX MAX COL
ind = 0
lenght = len(c)
main_nums = []
while ind != lenght:
    for c in test_matrix:
        nums.append(c[ind])
    nums_sum = sum(nums)
    main_nums.append(nums_sum)
    nums.clear()
    ind += 1
max_main = max(main_nums)
r_index = main_nums.index(max_main,0,b)
print(f"Индекс максимальной колонки - {r_index}")
nums.clear()
#INDEX MIN COL
ind = 0
lenght = len(c)
main_nums = []
while ind != lenght:
    for c in test_matrix:
        nums.append(c[ind])
    nums_sum = sum(nums)
    main_nums.append(nums_sum)
    nums.clear()
    ind += 1
min_main = min(main_nums)
r_index = main_nums.index(min_main,0,b)
print(f"Индекс минимальной колонки - {r_index}")
#Обнулить все элементы выше главной диагонали
r=[]
for i in range (n):
    v=[]
    for j in range (m):
        if i<j:
            v.append(0)
        else:
            v.append(randint(a,b))
    r.append(v)
for i in r:
    for m in i:
        print(m, end=' ')
    print()

#Обнулить все элементы ниже главной диагонали
r=[]
for i in range (4):
    v=[]
    for j in range (4):
        if i>j:
            v.append(0)
        else:
            v.append(randint(a,b))
    r.append(v)
for i in r:
    for m in i:
        print(m, end=' ')
    print()
