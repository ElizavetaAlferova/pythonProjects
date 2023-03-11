import json

with open("D:\\Downloads\\countries.json", encoding="utf-8") as f1, open("religion.json", "w", encoding="utf-8") as f2:
    content = json.load(f1)
    religions=[]
    for i in content:
        religions.append(i['religion'])
    print(content)
    religions=list(set(religions))
    country = {k: [i['country'] for i in content if i['religion']==k] for k in religions}
    new_dict = {}
   # country = {k: [[i['country'] for i in content if i['religion'] == j] for j in religions] for k in religions}
    #print(set(religions))

    json.dump(country, f2, indent=3)
