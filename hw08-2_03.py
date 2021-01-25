#Создать CSV фа л с данными о ежедневно погоде за
#10 дней для 3-х городов. Структура: Дата, Город,
#Температура, Скорость ветра.
#Создать отчетны фа л в формате CSV со структурой:
#Город, Средняя температура. Записать в него
#данные по каждому Городу. Данные в CSV файле
#должны быть отсортированы по возрастанию
#средней температуры.
import csv

with open('weather.csv',encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ',')
    count = 0
    i = 0
    temp = []
    w_list = []
    with open('weather_report.csv', mode='w',encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ',', lineterminator='\r\n')
        file_writer.writerow(['Город', 'Средняя Температура'])
        for row in file_reader:
            if count == 0:
                print(f'File has columns {", ".join(row)}')
            else:
                if row[1] == 'Минск':
                    temp.append(int(row[2]))
                    i += 1
                    if i == 10:
                        avg = sum(temp) / i
                        l = [row[1], avg]
                        w_list.append(l)
                        i = 0
                        temp.clear()
                if row[1] == 'Гродно':
                    temp.append(int(row[2]))
                    i += 1
                    if i == 10:
                        avg = sum(temp) / i
                        l = [row[1], avg]
                        w_list.append(l)
                        i = 0
                        temp.clear()
                if row[1] == 'Брест':
                    temp.append(int(row[2]))
                    i += 1
                    if i == 10:
                        avg = sum(temp) / i
                        l = [row[1], avg]
                        w_list.append(l)
                        i = 0
                        temp.clear()
                print(row)
            count += 1
        sorted_w_list = sorted(w_list, key=lambda temp: temp[1], reverse=True)
        file_writer.writerows(sorted_w_list)
        print(f'file has {count} strings')
