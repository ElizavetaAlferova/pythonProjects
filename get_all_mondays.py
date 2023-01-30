import calendar
from datetime import date, datetime, timedelta

def get_all_mondays(year:int)->list[date]:
    current_date = datetime(year=year, month=1, day=1).date()
    end_date=datetime(year=year+1, month=1, day=1).date()
    print(current_date)
    list_mondays=[]
    while current_date<end_date:
        if current_date.weekday() == 0:
            list_mondays.append(current_date)
        current_date=current_date+timedelta(days=1)
    return list_mondays

print(get_all_mondays(2021))