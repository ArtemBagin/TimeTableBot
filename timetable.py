import datetime
import json


class TimeTable:
    week_names = [
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница'
    ]
    table_time = [
        '09.00-10.35',
        '10.55-12.30',
        '13.00-14.35',
        '14.55-16:30',
        '16.50-1825'
    ]
    emptiness_message = 'Выходной'

    def __init__(self):
        with open('timetable.json', encoding='utf-8') as f:
            self.timetable = json.loads(f.read())

    def get_timedata(self, day, parity):
        data = self.timetable[str(day)][str(int(not parity))]
        if not data:
            return self.emptiness_message
        text = ''
        c = 1
        for i in data:
            if i:
                text += f'{c}. {self.table_time[c - 1]} {i}\n'
            c += 1
        return text

    def get_today_timedata(self):
        day = self.day_week()
        parity = self.parity_week()
        if int(day) > 5:
            return self.emptiness_message
        parity_status = 'чётная' if parity % 2 == 0 else 'нечётная'
        text = f'Расписание занятий на {self.week_names[day-1]}({parity_status} неделя):\n\n'
        return text + self.get_timedata(day, parity)

    def get_week_timedata(self):
        parity = self.parity_week()
        parity_status = 'чётная' if parity % 2 == 0 else 'нечётная'
        text = f'Расписание занятий на неделю({parity_status} неделя):\n\n'
        for day in range(1, 6):
            text += f'{self.week_names[day-1]}:\n{self.get_timedata(day, parity)}\n\n'
        return text

    def parity_week(self):
        return int(datetime.datetime.now().strftime("%V")) % 2

    def day_week(self):
        return datetime.datetime.today().isoweekday()
