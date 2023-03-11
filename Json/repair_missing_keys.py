import json

with open("D:\\Downloads\\people.json", encoding="utf-8") as f1:
    content1 = json.loads(f1.read())
    keys={}
    for i in content1:
        print(i)
        keys |= i
    print(keys.keys())
    for i in content1:
        for j in keys.keys():
            if j not in i.keys():
                i[j]=None

with open("updated_people.json", "w", encoding='utf-8') as total:
    json.dump(content1, total, indent =3)