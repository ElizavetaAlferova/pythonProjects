"""
Докажите, что 1313-е число месяца чаще всего приходится на пятницу.
 Напишите программу, которая вычисляет, сколько тринадцатых чисел приходится
  на каждый день недели в период с 01.01.0001 по 31.12.9999.

Формат выходных данных
Программа должна вывести 7 чисел — количество тринадцатых чисел, которые
приходятся на понедельник, вторник, среду, четверг, пятницу, субботу и воскресенье
в период с 01.01.0001 по 31.12.9999. Числа должны быть расположены каждое на отдельной строке.

"""

from datetime import date, time, datetime, timedelta

first_date = date(1, 1, 1)
end_date = date(9999, 12, 31)
dict_days = {}
while first_date < end_date:
    for i in range(7):
        if first_date.weekday() == i and first_date.day == 13:
            dict_days[i] = dict_days.get(i, 0) + 1
    first_date = first_date + timedelta(days=1)
sorted_tuple = sorted(dict_days.items(), key=lambda x: x[0])
print(*[i[1] for i in sorted_tuple], sep='\n')
