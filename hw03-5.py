
def rectangle():
    a = int(input("1: "))
    b = int(input("2: "))

    area = (a * b) / 2
    gip = (a ** 2) + (b ** 2)

    print(f"Площадь:{area}\nГипотенуза:{gip}")

if __name__ == "__main__":
    rectangle()