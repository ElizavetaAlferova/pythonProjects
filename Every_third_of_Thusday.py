import calendar
from datetime import datetime, date
year=int(input())
days = []
for month in range(1, 13):
    count=0
    for week in calendar.monthcalendar(year, month):
        # print(week)
        thu= week[3]
        if thu:
            count+=1
        if thu and count==3:
            days.append(date(year, month, thu))
print(*list(map(lambda x: datetime.strftime(x, "%d.%m.%Y"), days)), sep='\n')





