import csv


with open('D:\\Downloads\data.csv', encoding="utf-8") as file:
    rows = list(csv.DictReader(file, delimiter = ","))
with open("domain_usage.csv",'w',  encoding="utf-8") as csv_file:
    names = ["domain", "count"]
    writer = csv.writer(csv_file)
    writer.writerow(["domain", "count"])
    data=[]
    my_dict = {}
    for row in rows:
        email=row["email"]    #'johnwilson@outlook.com'
        my_dict[email[email.find("@")+1:]] = my_dict.get(email[email.find("@")+1:],0)+1

    sorted_tuples = sorted(my_dict.items(), key=lambda item: (item[1], item[0]))

    for i in sorted_tuples:
      data.append(list(i))

    writer.writerows(data)









