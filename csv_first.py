import csv

with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
    # создаем writer объект и указываем названия столбцов
    keys = ['first_col', 'second_col']
    data = [{"first_col":"value1","second_col":"value2"}]
    writer = csv.DictWriter(csv_file, fieldnames = keys,delimiter = ",")
    # записываем первую строку с названиями столбцов
    writer.writeheader()

    # записываем строку с данными
    for row in data:
        writer.writerow(row)