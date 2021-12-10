class WeekDayError(Exception):
    pass

class Weeker:
    diassemana = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    def __init__(self, day):
        if not day in Weeker.diassemana:
            raise WeekDayError()
        else:
            self.day = day
    
    def __str__(self):
        return self.day

    def add_days(self, n):
        self.n = n
        if self.n%7==0:
            self.day
        else:
            self.day = Weeker.diassemana[(Weeker.diassemana.index(self.day))+self.n%7]

    def subtract_days(self, n):
        
        self.n = n
        if self.n%7==0:
            self.day
        else:
            self.day = Weeker.diassemana[(Weeker.diassemana.index(self.day))-self.n%7]

try:

    weekday = Weeker("Mon")
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(2)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")