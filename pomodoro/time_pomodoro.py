from datetime import time
import time


class Pomodoro:

    def __init__(self, focus_time=25, break_time=5, cycle=4):
        self.focus_time = focus_time
        self.break_time = break_time
        self.cycle = cycle
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.c_focus_time = focus_time
        self.c_break_time = break_time

    def f_seconds_g(self):
        """Генератор секунд"""
        while self.seconds > 0:
            self.seconds -= 1
            yield f"Осталось работать: {self.hours}:{self.focus_time}:{self.seconds}"

    def b_seconds_g(self):
        """Генератор секунд"""
        while self.seconds > 0:
            self.seconds -= 1
            yield f"Осталось отдыха: {self.hours}:{self.break_time}:{self.seconds}"

    def minutes_g(self):
        """Генератор минуты"""
        while self.minutes > 0:
            self.minutes -= 1
            self.seconds += 60
            yield f"Осталось времени: {self.hours}:{self.minutes}:{self.seconds}"

    def focus_g(self):
        """Генератор минуты"""
        while self.focus_time > 0:
            self.focus_time -= 1
            self.seconds += 60
            yield f"Осталось работать: {self.hours}:{self.focus_time}:{self.seconds}"

    def break_g(self):
        """Генератор минуты"""
        while self.break_time > 0:
            self.break_time -= 1
            self.seconds += 60
            yield f"Осталось отдыха: {self.hours}:{self.break_time}:{self.seconds}"

    def hours_g(self):
        """Генератор часы"""
        while self.hours > 0:
            self.hours -= 1
            self.minutes += 59
            self.seconds += 60
            yield f"Осталось времени: {self.hours}:{self.minutes}:{self.seconds}"

    def cycle_g(self):
        """cycle generator"""
        while self.cycle > 0:
            self.cycle -= 1
            self.focus_time = self.c_focus_time
            self.break_time = self.c_break_time
            yield f'Осталось повторений {self.cycle}'

    def pomodoro_func(self):
        while self.focus_time > 0 and self.break_time > 0 and self.cycle > 0:
            if self.focus_time > 0:
                print(f'DO THIS FOR A {self.focus_time} minutes LONG')
                while self.hours > 0 or self.focus_time > 0 or self.seconds > 0:
                    if self.seconds > 0:
                        print(next(Pomodoro.f_seconds_g(self)))
                        # time.sleep(1)
                        time.sleep(0.1)
                    if self.seconds == 0 and self.focus_time > 0:
                        print(next(Pomodoro.focus_g(self)))
                    if self.seconds == 0 and self.focus_time == 0 and self.hours > 0:
                        print(next(Pomodoro.hours_g(self)))
                else:
                    print('ALARM!!! ALARM!!! ALARM!!!')
            if self.focus_time == 0 and self.break_time > 0:
                print(f'TAKE A BREAK FOR {self.break_time} minutes')
                while self.hours > 0 or self.break_time > 0 or self.seconds > 0:
                    if self.seconds > 0:
                        print(next(Pomodoro.b_seconds_g(self)))
                        # time.sleep(1)
                        time.sleep(0.1)
                    if self.seconds == 0 and self.break_time > 0:
                        print(next(Pomodoro.break_g(self)))
                    if self.seconds == 0 and self.focus_time == 0 and self.hours > 0:
                        print(next(Pomodoro.hours_g(self)))
                else:
                    print('ALARM!!! ALARM!!! ALARM!!!')
            if self.focus_time == 0 and self.break_time == 0 and self.cycle > 0:
                print(next(Pomodoro.cycle_g(self)))
