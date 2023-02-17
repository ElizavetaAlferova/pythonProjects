from calendar import monthcalendar
import datetime
year=int(input())
days = []
for month in range(1, 13):
    count: int=0
    for week in monthcalendar(year, month):
        # print(week)
        thu= week[3]
        if thu:
            count+=1
        if thu and count==3:
            days.append(datetime.date(year, month, thu))
print(*list(map(lambda x: datetime.datetime.strftime(x, "%d.%m.%Y"), days)), sep='\n')





