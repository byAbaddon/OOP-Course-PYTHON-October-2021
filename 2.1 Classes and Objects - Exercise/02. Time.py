from datetime import datetime, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time = datetime(2020, 7, 1, self.hours, self.minutes, self.seconds)

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return str(self.time)[-8:]

    def next_second(self):
        self.time = self.time + timedelta(0, 1)
        return self.get_time()


# ------------------------------------
time = Time(9, 30, 59)
print(time.next_second())

'''
09:31:00
'''
