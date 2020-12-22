#Даны 2 действительных числа a и b. Получить их сумму, разность и произведение.

# 1 вариант
a = 5
b = 4

summ = a + b
division = a / b
multuply = a * b

print(f"Сумма: {summ}")
print(f"Деление: {division}")
print(f"Умножение: {multuply}")
# 2 вариант
(lambda x, y: x + b)(a, b)
(lambda x, y: x / b)(a, b)
(lambda x, y: x * b)(a, b)

# 3 вариант

def math():
    f_num = int(input("Введите первое число: "))
    s_num = int(input("Введите второе число: "))

    summ_2 = f_num + s_num
    division_2 = f_num / s_num
    multuply_2 = f_num * s_num

    print(f"Сумма: {summ_2}\nДеление: {division_2}\nУмножение: {multuply_2}\n")

    
if __name__ == "__main__":
    math()



