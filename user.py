from datetime import datetime, date, time
import csv


def author():
    pass


class User:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def init_user(self):
        with open('log.csv', mode='a', encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ',', lineterminator='\r\n')
            file_writer.writerow([self.name, self.surname, self.time])

    def __repr__(self):
        return f'Name - {self.name}, Surname - {self.surname}, Time - {self.time}'
