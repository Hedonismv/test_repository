#Дан список. Создать новы список, сдвинуты на 1
#элемент влево Пример:12345 -> 23451
def main():
    numbers = [1,2,3,4,5]
    new_numbers = []
    i = len(numbers)
    v = i - 1
    while v < i:
        new_numbers = numbers
        new_numbers.append(numbers[0])
        new_numbers.remove(numbers[0])
        v += 1
    print(f"Новый список:  {new_numbers}")

if __name__ == '__main__':
    main()
