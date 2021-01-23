#Создать CSV фа л с данными следующе структуры:
#Имя, Фамилия, Возраст. Создать отчетны фа л в
#формате CSV с информацие по количеству люде
#входящих в ту или иную возрастную группу.
#Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.

import csv



with open('peoples.csv', encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ',')
    with open('report.csv', mode='w',encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ',', lineterminator='\r\n')
        file_writer.writerow(['Имя','Фамилия','Возраст','Возрастная группа'])
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'Файл содержит столбцы: {", ".join(row)}')
            elif count != 0:
                if int(row[2]) > 40:
                    file_writer.writerow([row[0],row[1],row[2],'группа 40+ лет'])
                    print('40+')
                elif int(row[2]) >= 26 and int(row[2]) <= 40:
                    file_writer.writerow([row[0],row[1],row[2],'группа 26-40 лет'])
                    print('26-40')
                elif int(row[2]) >= 19 and int(row[2]) <= 25:
                    file_writer.writerow([row[0],row[1],row[2],'группа 19-25 лет'])
                    print('19-25')
                elif int(row[2]) >= 13 and int(row[2]) <= 18:
                    file_writer.writerow([row[0],row[1],row[2],'группа 13-18 лет'])
                    print('13-18')
                elif int(row[2]) >= 1 and int(row[2]) <= 12:
                    file_writer.writerow([row[0],row[1],row[2],'группа 1-12 лет'])
                    print('1-12')
                else:
                    print('ELSE')
            count += 1
    print(f'В файле {count} строк. Все данные отсортированы и внесены.')
