import calendar
from datetime import datetime, date

def get_days_in_month(year: int, month)-> list[date]:
    mon = list(calendar.month_name)
    count_days=calendar.monthrange(int(year), mon.index(month))[1]
    list_days = []
    d=1
    for i in range(count_days):
        list_days.append(datetime(year=int(year), month = mon.index(month), day = d).date())
        d+=1
    return list_days


y, m = input().split()
print(get_days_in_month(y, m))