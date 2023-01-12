"""
реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:
dates — список строковых дат в формате DD.MM.YYYY
Функция должна возвращать список, в котором содержатся все даты из
 списка dates, расположенные в порядке возрастания, а также все недостающие промежуточные даты.
примечание 1. Рассмотрим первый тест. Список dates содержит период с 01.11.2021 по 07.11.2021:
dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
в котором отсутствуют даты 02.11.2021, 05.11.2021, 06.11.2021. Тогда вызов функции:
"""

from datetime import datetime, timedelta


def Fill_up(dates):
    '''I write comment'''
    sample = '%d.%m.%Y'
    dates = list(map(lambda x: datetime.strptime(x, sample), dates))
    max_date = max(dates)
    min_date = min(dates)
    blank_list = []
    while min_date <= max_date:
        blank_list.append(datetime.strftime(min_date.date(), sample))
        min_date = min_date + timedelta(days=1)
    return blank_list


d = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(Fill_up(d))
