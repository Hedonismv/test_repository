#Дан текстовый фа л, содержащи различные даты.
#Каждая дата - это число, месяц и год. На ти самую
#раннюю дату.
from datetime import datetime, date, time


def read_lines(file_name):
    with open(file_name,'r') as f:
        length = len(f.readlines())
    file = open(file_name,'r')
    i = 0
    dates = []
    while i < length:
        line = file.readline().rstrip()
        print(line)
        d = datetime.strptime(line,"%d-%m-%Y")
        dates.append(d)
        i += 1
    print("Самая ранняя дата - {}".format(min(dates)))
    file.close()


read_lines('test.txt')
