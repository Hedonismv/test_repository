# Дан список строк. Отформатировать все строки в
# формате ‘{i} - {string}’, где i это порядковы номер
# строки в списке. Использовать генератор списков.
words = 'string', 'word', 'forar', 'grades'
lists = [a for a in words]
i = 1
for string in lists:
    print(f"{i} - {string}")
    i += 1
