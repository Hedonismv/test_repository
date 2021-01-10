#Дан список целых чисел.
#Создать новы список, кажды элемент которого равен
#исходному элементу умноженному на -2
def main():
    list = [1, 5, 6, 3, 9]
    new_list = []
    for n in list:
        result = n * -2
        new_list.append(result)
    print(f"Method for: {new_list}")

def second():
    numbers = [1, 5, 6, 3, 9]
    new_numbers = []
    i = len(numbers)
    v = 0
    while v < i:
        result = numbers[v] * -2
        new_numbers.append(result)
        v += 1
        continue
    print(f"Method While: {new_numbers}")

if __name__ == '__main__':
    main()
    second()
