import os
import datetime

import dateutil

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
homework_path = os.path.join(base_path, 'eugene_okulik', 'hw_13', 'data.txt')
week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

with open(homework_path, 'r') as read_file:
    homework_file = read_file.read()
    for line in homework_file.splitlines():
        if '1.' in line:
            parts_1 = line.split(' - ')
            line_1 = parts_1[0].strip('1. ')
            line_date_1 = dateutil.parser.parse(line_1)
            print(line_date_1 + datetime.timedelta(days=7))
        elif '2.' in line:
            parts_2 = line.split(' - ')
            line_2 = parts_2[0].strip('2.')
            line_date_2 = dateutil.parser.parse(line_2)
            print(week[line_date_2.isoweekday()])
        elif '3.' in line:
            now = datetime.datetime.now()
            parts_3 = line.split(' - ')
            line_3 = parts_3[0].strip('3. ')
            line_date_3 = dateutil.parser.parse(line_3)
            date = now - line_date_3
            print(f'Это было {date.days} дня назад')
