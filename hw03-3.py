#Дана длина ребра куба. На ти объем куба и площадь его боково поверхности.

def cube():
    s = int(input("Введите длинну ребра куба: "))
    p = s * s
    v = s * s * s

    print(f"Длинна ребра: {s}\nПлощадь стороны: {p}\nОбъем куба: {v}\n")

if __name__ == "__main__":
    cube()