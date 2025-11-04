import datetime


human_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(human_date, "%b %d, %Y - %I:%M:%S")
month = datetime.datetime.strftime(python_date, "%B")
new_date = datetime.datetime.strftime(python_date, '"%d.%m.%Y, %I:%M"')
print(python_date)
print(month)
print(new_date)
