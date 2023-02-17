import csv


with open('D:\\Downloads\\titanic.csv', encoding="utf-8") as file:
    rows = csv.DictReader(file, delimiter =";")
    names_male=[]
    names_female=[]
    for row in rows:

        if row["survived"]=="1" and float(row["age"])<18:
            if row["sex"]=="male":
                names_male.append(row["name"])
            else:
                names_female.append(row["name"])
    print(*names_male, sep='\n')
    print(*names_female, sep='\n')

