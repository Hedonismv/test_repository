#Для каждого натурального числа в промежутке от m до
#n вывести все делители, кроме единицы и самого
#числа. m и n вводятся с клавиатуры.
#Пример:m =100, n = 105

m = int(input("От: "))
n = int(input("До: "))
n+=1
for i in range(m,n):
    for num in range(2, i):
        if i % num == 0:
            print(f"{i}: {num}")
