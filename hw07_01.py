# Описать функцию fact2(n), вычисляющую дво но
# факториал: n!! = 1·3·5·...·n, если n — нечетное; n!! =
# 2·4·6·...·n, если n — четное (n > 0 — параметр целого
# типа). С помощью это функции на ти дво ные
# факториалы пяти случайных целых чисел.
import sys, pytest
from os.path import dirname as d
from os.path import abspath, join

root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)


def test_fact2(n: int) -> int:
    """Функция вычисляет факториал числа N, в завимисимости
от того четное оно или нет 
    """
    assert type(n) == int, 'Должно быть введено целое число'
    start = 1 if n % 2 else 2
    for i in range(start + 2, n + 1, 2):
        start *= i
    print(start)


test_fact2(14)
