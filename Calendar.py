import calendar
from datetime import datetime
m = list(calendar.month_name)
# m = list(calendar.month_abbr)
# year, month = input().split()
# print(calendar.month(int(year), m.index(month)))

# d = datetime.strptime(input(), '%Y-%m-%d')
# day = calendar.weekday(d.year, d.month, d.day)
# print(calendar.day_name[day])

year, month = input().split()
print(calendar.monthrange(int(year), m.index(month))[1])