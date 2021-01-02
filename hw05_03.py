#Дано число. На ти сумму и произведение его цифр.

def main():
    x = input("Введите минимум двузначное число:" )
    #lenght = len(x)
    summ = 0
    multy = 1
    pack = []
    if len(x) > 1:
        for i in x:
            pack.append(i)
        for v in pack:
            summ = summ + int(v)
        for v in pack:
            multy = multy * int(v)
        print(f"Сумма: {summ}\nПроизведение: {multy}")
    else:
        print("ne norm")


if __name__ == '__main__':
    main()
