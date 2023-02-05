import csv

with open("D:\\Downloads\\salary_data.csv", encoding="utf-8") as csv_file:
    rows = csv.DictReader(csv_file, delimiter=';')  # создаем reader объект
    sum_salary_dict={}
    count_dict={}
    finish_dict={}
    for row in rows:
        sum_salary_dict[row["company_name"]]=sum_salary_dict.get(row["company_name"], 0)+ int(row["salary"])
        count_dict[row["company_name"]]=count_dict.get(row["company_name"], 0)+1
    for i in sum_salary_dict:
        finish_dict[i] = sum_salary_dict[i]/count_dict[i]
    for i in sorted(finish_dict.items(), key=lambda item: (item[1], item[0])):
        print(i)



