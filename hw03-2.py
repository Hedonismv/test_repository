#Даны действительные числа х и у получить х - у  и  1+ ху

#1 вариант

x = 2
y = 4

result = (x - y) / (1 + (x * y))
print(f"1st result: {result}")

# 2 вариант
def res():
    f_num = int(input("Введите первое число: "))
    s_num = int(input("Введите второе число: "))

    result_2 = (f_num - s_num) / (1 + (f_num * s_num))

    print(f"Func result {result_2}")


if __name__ == "__main__":
    res()