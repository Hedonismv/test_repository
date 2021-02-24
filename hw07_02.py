# Даны три слова. Выяснить, является ли хоть одно из
# них палиндромом ("перевертышем"), т. е. таким,
# которое читается одинаково слева направо и справа
# налево. (Определить функцию, позволяющую
# распознавать слова палиндромы.)

def palindrome(a: str, b: str, c: str) -> str:
    """Функция проверяет является ли слово палиндромом
в функцию обязательно передайте 3 аругмента формата строки
    """
    assert type(a) == str and type(b) == str and type(c) == str, 'Должно быть STR'
    for word in a, b, c:
        pal = word[::-1]
        if word == pal:
            print(f"{word} is a palindrome!")
        else:
            print(f"{word} NOT A PALINDROME")


palindrome('ala', 'baab', 'word')
