import json
import csv
with open("D:\\Downloads\\students.json", encoding="utf-8") as f1, open("data.csv", "w", encoding="utf-8", newline='') as f2:
    content = json.loads(f1.read())
    headers=["name", "phone"]
    writer = csv.writer(f2, delimiter=",")
    writer.writerow(headers)
    data=[]
    for i in content:
        if i['age']>=18 and i['progress']>=75:
            data.append([i['name'], i['phone']])
    data = sorted(data,key = lambda x: x[0])
    writer.writerows(data)
    print(data)
    print(content)