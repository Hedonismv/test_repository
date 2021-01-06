#В заданно строке расположить в обратном порядке
#все слова. Разделителями слов считаются пробелы.

words = ["qwerty","Fendi","Ritter","Poll","Kitana","Luke"]

words.reverse()
edited_str = ""
for string in words:
    new_string = str(string)
    new_string = new_string.replace(',','')
    edited_str += new_string + ' '
print(edited_str)
