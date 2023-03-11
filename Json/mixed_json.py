import json

with open("D:\\Downloads\\data1.json", encoding="utf-8") as f1, open("D:\\Downloads\\data2.json", encoding="utf-8") as f2:
    content1 = json.loads(f1.read())

    content2=json.loads(f2.read())

    content1 |=content2 # конкатенация словерей (можно было через content1.update(content2)), при совпадении ключей идет значение из 2 словаря

with open("data_merge.json", "w", encoding='utf-8') as total:
    json.dump(content1, total, indent =3)