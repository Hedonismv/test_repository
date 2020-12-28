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

def second():
    numbers = [1, 4, 6, 9, 5, 8]
    i = len(numbers)
    v = 0
    c = 0
    while v < i:
        if numbers[v] %2 == 0:
            c += 1
            v += 1
        else:
            v += 1
            continue
    print(f"Количество четных чисел в строке: {c}")


if __name__ == '__main__':
    second()
