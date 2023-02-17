import csv

with open("D:\\Downloads\\student_counts.csv", encoding="utf-8") as f:
    rows = csv.DictReader(f)
    columns = rows.fieldnames
    sorted_columns = sorted(columns[1:], key =lambda x: (int(x[:x.find("-")]), x[x.find("-"):]))
    # print([columns[0]]+(sorted_columns))
    sorted_columns = [columns[0]]+(sorted_columns)
    # for row in rows:
    #     print(row)
    rows=list(rows)
with open("sorted_student_counts.csv", "w", encoding="utf-8", newline='') as csv_file:
    writer=csv.writer(csv_file)
    data=[]
    for row in rows:
        l = []
        for sorted_column in sorted_columns:
            l+=[row[sorted_column]]
        data.append(l)
    # print(data)
    writer.writerow(sorted_columns)
    writer.writerows(data)


