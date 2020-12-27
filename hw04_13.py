#Дан список. Создать новы список, сдвинуты на 1
#элемент влево Пример:12345 -> 23451
numbers = [1,2,3,4,5]
numbers.append(numbers[0])
numbers.remove(numbers[0])
print(numbers)
