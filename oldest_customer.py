"""
.rfind(' ') + 1
На вход программе в первой строке подается натуральное число nn —
количество сотрудников, работающих в организации. В последующих nn
строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения,
 разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна определить самого старшего сотрудника и вывести его дату
 рождения, имя и фамилию, разделив пробелом. Если таких сотрудников несколько,
  программа должна вывести их дату рождения, а также их количество, разделив пробелом.
"""
from datetime import datetime
pattern = '%d.%m.%Y'
n = int(input())
list_of_customers = []
oldest = []
for i in range(n):
    list_of_customers.append(input().split())
more_old = datetime(year=9999, month=1, day=1)
for i in list_of_customers:
    if datetime.strptime(i[2], pattern) <= more_old:
        more_old = datetime.strptime(i[2], pattern)
        oldest = i
count = 0
for i in list_of_customers:
    if i[2] == oldest[2]:
        count += 1
if count == 1:
    print(f'{oldest[2]} {oldest[0]} {oldest[1]}')
else:
    print(f'{oldest[2]} {count}')
