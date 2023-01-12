"""
Репетитор по математике проводит занятия по 45 минут с перерывами по 10 минут.
 Репетитор обозначает время начала рабочего дня и время окончания рабочего дня.
 Напишите программу, которая генерирует и выводит расписание занятий.

Формат входных данных
На вход программе в первой строке подается время начала рабочего дня в формате HH:MM.
В следующей строке вводится время окончания рабочего дня в том же формате.

Формат выходных данных
Программа должна сгенерировать и вывести расписание занятий. На первой строке выводится
 время начала и окончания первого занятия в формате HH:MM - HH:MM, на второй строке —
 время начала и окончания второго занятия в том же формате, и так далее.

Примечание 1. Если занятие обрывается временем окончания работы, то добавлять его в
расписание не нужно.

Примечание 2. Если разница между временем начала и окончания рабочего дня меньше
45 минут, программа ничего не должна выводить.

"""
from datetime import datetime, timedelta

pattern = '%H:%M'
start_time = datetime.strptime(input(), pattern)
end_time = datetime.strptime(input(), pattern)

schedule = []
while end_time >= start_time:
    if start_time + timedelta(minutes=45) <= end_time:

        print(datetime.strftime(start_time, pattern), end=' - ')
        print(datetime.strftime(start_time + timedelta(minutes=45), pattern))
        start_time = start_time + timedelta(minutes=55)
    else:
        break
