import json
with open("D:\\Downloads\\data.json", encoding='utf-8') as file:
    content = json.loads(file.read())
with open("../updated_data.json", 'w', encoding='utf-8') as file:
    finish_list=[]
    for i in content:
        if type(i)==str:
            i=i+"!"
            finish_list.append(i)
        elif i is None:
            continue
        elif type(i)==int or type(i)==float:
            i+=1
            finish_list.append(i)
        elif type(i)==bool:
            i=not(i)
            finish_list.append(i)
        elif type(i)==list:
            i = i*2;
            finish_list.append(i)
        elif type(i)==dict:
            i.update({"newkey": None})
            finish_list.append(i)
    json.dump(finish_list, file, indent=3)



    # for row in rows:
        # print(row)
    # print(finish_list)
