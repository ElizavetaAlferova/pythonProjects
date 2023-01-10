from datetime import datetime, date, timedelta

pattern='%d.%m.%Y'
start_date=datetime.strptime(input(), pattern)
end_date = datetime.strptime(input(), pattern)

"""
Напишите программу, которая из этого диапазона,
 включая границы, выводит, начиная с даты, у которой 
 сумма дня и месяца нечетная, каждую третью дату, только если она не понедельник и не четверг.
"""
f = True
while f:
    if (start_date.day+start_date.month)%2!=0:
        first_date = start_date
        f = False
    else:
        start_date+=timedelta(days=1)
while first_date<=end_date:
    if first_date.weekday() not in [0, 3]:
        print(datetime.strftime(first_date, pattern))
    first_date+=timedelta(days=3)



