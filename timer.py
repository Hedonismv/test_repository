from datetime import datetime, date, time
import time


class Timer:

    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def seconds_g(self):
        """Генератор секунд"""
        while self.seconds > 0:
            self.seconds -= 1
            yield f"Осталось времени: {self.hours}:{self.minutes}:{self.seconds}"

    def minutes_g(self):
        """Генератор минуты"""
        while self.minutes > 0:
            self.minutes -= 1
            self.seconds += 60
            yield f"Осталось времени: {self.hours}:{self.minutes}:{self.seconds}"

    def hours_g(self):
        """Генератор часы"""
        while self.hours > 0:
            self.hours -= 1
            self.minutes += 59
            self.seconds += 60
            yield f"Осталось времени: {self.hours}:{self.minutes}:{self.seconds}"


    def start_timer(self):
        """Основная функция запуска таймера"""
        while self.hours > 0 or self.minutes > 0 or self.seconds > 0:
            if self.seconds > 0:
                print(next(Timer.seconds_g(self)))
                time.sleep(1)
                #time.sleep(0.1) Test HOURS working
            if self.seconds == 0 and self.minutes > 0:
                print(next(Timer.minutes_g(self)))
            if self.seconds == 0 and self.minutes == 0 and self.hours > 0:
                print(next(Timer.hours_g(self)))
        else:
            print('ALARM!!! ALARM!!! ALARM!!!')



    def __repr__(self):
        return f"Remaining time: {self.hours}:{self.minutes}:{self.seconds}"
