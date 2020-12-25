#Дан список целых чисел. Подсчитать сколько четных
#чисел в списке

def main():
    list = [1, 4, 6, 9, 5, 8]
    numbers = 0
    for n in list:
        if n %2 == 0:
            numbers += 1
        else:
            continue
    print(f"Количество четных чисел в строке: {numbers}")

if __name__ == '__main__':
    main()
