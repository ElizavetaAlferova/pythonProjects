'''
На вход программе подается последовательность дат, разделенных пробелом, в формате DD.MM.YYYY.

Формат выходных данных
Программа должна вывести список, содержащий неотрицательные целые числа,
 каждое из которых — количество дней между двумя соседними датами последовательности.

'''

from datetime import datetime, timedelta, date
sample='%d.%m.%Y'
diff_neighbor=[]

list_dates=[datetime.strptime(i, sample) for i in input().split()]
for i in range(len(list_dates)-1):
    diff_neighbor.append(abs(list_dates[i]-list_dates[i+1]).days)


print(diff_neighbor)
print(list_dates)