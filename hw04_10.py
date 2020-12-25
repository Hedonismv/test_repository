#Дан список целых чисел.
#Создать новы список, кажды элемент которого равен
#исходному элементу умноженному на -2
def main():
    list = [1, 5, 6, 3, 9]
    new_list = []
    for n in list:
        result = n * -2
        new_list.append(result)
    print(new_list)

if __name__ == '__main__':
    main()
