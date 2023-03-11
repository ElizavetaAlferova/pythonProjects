import json
import csv

with open("D:\\Downloads\\playgrounds.csv", encoding="utf-8") as f1, open("addresses.json", "w", encoding="utf-8") as f2:
    content = list(csv.DictReader(f1, delimiter = ';'))
    print(content)
    d ={}
    for i in content:
        d.setdefault(i["AdmArea"], {}).setdefault(i["District"], []).append(i["Address"])
    json.dump(d, f2, indent=3, ensure_ascii=False)
    print(d)



