#Ввести строку. Если длина строки больше 10
#символов, то создать новую строку, равную текущей, с
#3 восклицательными знаками в конце ('!!!') и вывести
#на экран. Если меньше 10, то вывести на экран второ
#символ строки.

def length():
    string = input("Введите строку: \n")

    if len(string) > 10:
        a_string = string + "!!!"
        print(f"{a_string}")
    elif len(string) < 10:
        s_string = string[1]
        print(f"Второй символ строки: {s_string}")

if __name__ == '__main__':
    length()
