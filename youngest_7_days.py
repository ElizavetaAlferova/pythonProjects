"""
Дан список сотрудников организации, в котором указаны их фамилии,
 имена и даты рождения. Напишите программу, которая определяет самого
  молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней от текущей даты.
Формат входных данных
На вход программе в первой строке подается текущая дата в формате
 DD.MM.YYYY, в следующей строке вводится натуральное число nn — количество
  сотрудников, работающих в организации. В последующих nn строках вводятся данные
   о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробело
   м. Дата рождения указывается в формате DD.MM.YYYY.
Формат выходных данных
Программа должна определить самого молодого сотрудника, празднующего
 свой день рождения в течение ближайших семи дней, и вывести его имя и фамилию,
  разделив пробелом. Если таких сотрудников нет, программа должна вывести текст:
"""

from datetime import datetime, timedelta, date, time

pattern = "%d.%m.%Y"
current_date = datetime.strptime(input(), pattern)+timedelta(days=1)  # формат дата
end_date = current_date + timedelta(days=6)
n = int(input())  #count customers
list_of_customers = []
for i in range(n):

    list_of_customers.append(input().split()) # где дата в формате строки pattern
    # list_of_customers.append(datetime.strptime(input().split()[2], pattern))
list_of_celebrant = []
while current_date<=end_date:
    for i in list_of_customers:
        # print(datetime.strptime(i[2], pattern))
        if datetime.strptime(i[2], pattern).month == current_date.month and datetime.strptime(i[2], pattern).day == current_date.day:
            list_of_celebrant.append(i) # список формата [['Петр', 'Сергеев', '14.11.1997'], ['Иван', 'Петров', '16.11.1995'], ['Сергей', 'Романов', '17.11.1994']]
    current_date+=timedelta(days=1)
# print(list_of_celebrant)
if list_of_celebrant!=[]:
    youngest = datetime.strptime(list_of_celebrant[0][2], pattern)
    # print(yangest) # 1997-11-14 00:00:00
    yang_list_str = list_of_celebrant[0]  # типа ['Петр', 'Сергеев', '14.11.1997']
    for i in list_of_celebrant:
        if datetime.strptime(i[2], pattern) > youngest:
            youngest = datetime.strptime((i[2]), pattern)
            yang_list_str = i
    print(*yang_list_str[:2])
else:
    print("Дни рождения не планируются")


# print(list_of_customers)













