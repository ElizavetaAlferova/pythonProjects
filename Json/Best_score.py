import json, csv
from datetime import datetime, date

with open("D:\\Downloads\\exam_results.csv", encoding='utf-8') as file, open("best_scores.json","w",encoding='utf-8') as f2:

    content = list(csv.DictReader(file))
    data =[]
    my_dict={}
    for i in content:
        if i['email'] in my_dict.keys():
            my_dict[i['email']] = i['score']
        else:
            my_dict[i["email"]] = my_dict.get(i["email"], i['score'])
    for i in content:
        if i['email'] in my_dict.keys() and i['score'] >= my_dict[i['email']]:
            data.append(i)

    for j in data:
        for k in data:

            if j['email']== k['email'] and datetime.strptime(j['date_and_time'], "%Y-%m-%d %H:%M:%S")>datetime.strptime(k['date_and_time'], "%Y-%m-%d %H:%M:%S"):
                if j['score']<k['score']:
                    data.remove(j)
                else:
                    data.remove(k)
            elif j['email']== k['email'] and datetime.strptime(j['date_and_time'], "%Y-%m-%d %H:%M:%S")<datetime.strptime(k['date_and_time'], "%Y-%m-%d %H:%M:%S"):
                if j['score']<=k['score']:
                    data.remove(j)
                else:
                    data.remove(k)

    d=[]
    sorted_tuples = dict(sorted(my_dict.items(), key=lambda item: (item[0], item[1])))
    sorted_list = sorted(data, key = lambda x: x['email'])
    for j in sorted_list:
        p={}
        p['name']= j.pop("name")
        p['surname'] = j.pop("surname")
        p["best_score"] = int(j.pop("score"))
        p['date_and_time'] = j.pop("date_and_time")
        p['email'] = j.pop("email")
        d.append(p)
    n = d.copy()
    for i in range(len(d)-1):
        if d[i]['email']==d[i+1]['email']:
            n.remove(d[i+1])



    json.dump(n, f2, indent=3)

