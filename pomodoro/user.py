from datetime import datetime, date, time
import csv


class User:

    def __init__(self, name, surname, task):
        self.name = name
        self.surname = surname
        self.task = task
        self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def init_user(self):
        with open('log.csv', mode='a', encoding='utf-8') as a_file:
            file_writer = csv.writer(a_file, delimiter=',', lineterminator='\r\n')
            file_writer.writerow([self.name, self.surname, self.time, self.task])

    def __repr__(self):
        return f'Name - {self.name}, Surname - {self.surname}, Time - {self.time}, Task - {self.task}'
