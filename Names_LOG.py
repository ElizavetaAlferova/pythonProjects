from datetime import date, datetime
import csv

with open("D:\\Downloads\\name_log.csv", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))
with open("new_name_log", "w", encoding="utf-8") as new_file:
    writer = csv.writer(new_file)
    writer.writerow(["username", "email", "dtime"])
    names_dict={}
    finish={}
    for row in rows:
        names_dict[row["email"]] = names_dict.get(row["email"], [])+[[row["username"], row["dtime"]]]
    for key, value in names_dict.items():
        sorted_tup=sorted(value, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y %H:%M"), reverse=True)

        finish[key]=sorted_tup[0]

    finish_2=[]
    finish_sorted=sorted(finish.items(), key = lambda x: x[0])

    for i in finish_sorted:
        fi=[]
        fi.append(i[1][0])
        fi.append(i[0])
        fi.append(i[1][1])
        finish_2.append(fi)
    writer.writerows(finish_2)
