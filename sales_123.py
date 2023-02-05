import csv

with open("D:\\Downloads\\sales.csv", encoding="utf-8") as csv_file:
    rows = csv.reader(csv_file, delimiter=';')  # создаем reader объект
    rows=list(rows)
    for row in rows[1:]:
        if int(row[2])<int(row[1]):
            print(row[0])
