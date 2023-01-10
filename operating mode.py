"""
Напишите программу, которая принимает на вход текущие дату и время и определяет
количество минут, оставшееся до закрытия магазина.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести количество минут, которое осталось до закрытия магазина,
или текст Магазин не работает, если он закрыт.
"""
from datetime import datetime, timedelta

schedule = {0: (9, 21), 1: (9, 21), 2: (9, 21), 3: (9, 21), 4: (9, 21), 5: (10, 18), 6: (10, 18)}
pattern = '%d.%m.%Y %H:%M'
current_date = datetime.strptime(input(), pattern)
for key in schedule:

    if current_date<datetime(day = current_date.day, year=current_date.year, month=current_date.month, hour=schedule[key][0])\
            or current_date>=datetime(day = current_date.day, year=current_date.year, month=current_date.month, hour=schedule[key][1]):
        print("Магазин не работает")
    else:
        a=((datetime(day=current_date.day, year=current_date.year, month=current_date.month, hour=schedule[key][1])-current_date).total_seconds()//60)
        print(int(a))





