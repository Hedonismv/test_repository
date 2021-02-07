from datetime import datetime, date, time
import time_pomodoro


class Timer:

    def __init__(self, hours=0, minutes=0, seconds=0):
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
                # time.sleep(0.1) Test HOURS working
            if self.seconds == 0 and self.minutes > 0:
                print(next(Timer.minutes_g(self)))
            if self.seconds == 0 and self.minutes == 0 and self.hours > 0:
                print(next(Timer.hours_g(self)))
        else:
            print('ALARM!!! ALARM!!! ALARM!!!')


class Pomodoro(Timer):

    def __init__(self, focus_time=25, break_time=5, cycle=4):
        self.focus_time = focus_time
        self.break_time = break_time
        self.cycle = cycle

    def cycle_g(self):
        while self.cycle > 0:
            self.cycle -= 1
            self.focus_time += 25
            self.break_time += 5

    def pomodoro_func(self):
        while self.focus_time > 0 and self.break_time > 0 and self.cycle > 0:
            if self.focus_time > 0:
                self.minutes = self.focus_time
                Timer.start_timer()
            if self.focus_time == 0 and self.break_time > 0:
                self.minutes = self.break_time
                Timer.start_timer()
            if self.focus_time == 0 and self.break_time == 0 and self.cycle > 0:
                next(Pomodoro.cycle_g(self))

    def seconds_g(self):
        while self.seconds > 0:
            self.seconds -= 1
            yield f"Осталось времени: {self.hours}:{self.minutes}:{self.seconds}"

    def minutes_g(self):
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
