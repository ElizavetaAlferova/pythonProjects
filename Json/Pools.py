import json
from datetime import datetime, date, time

with open("D:\\Downloads\\pools.json", encoding='utf-8') as file:
    content = json.load(file)
    data =[]
    for i in content:
        time_open = datetime.strptime(i["WorkingHoursSummer"]['Понедельник'][:5], '%H:%M')
        time_close = datetime.strptime(i["WorkingHoursSummer"]['Понедельник'][6:], '%H:%M')
        if time_open.time()<=time(hour=10) and time_close.time()>=time(hour=12):
            data.append([i['DimensionsSummer']['Length'], i['DimensionsSummer']['Width'], i['Address']])
        # print(delta)
        # print(time_open)
        # print(time_close)
    #print(content)
    sorted_data = sorted(data, key = lambda x:(x[0], x[1]), reverse = True)

    print(f'{sorted_data[0][0]}x{sorted_data[0][1]}\n{sorted_data[0][2]}')
    # sorted_tuples = sorted(my_dict.items(), key=lambda item: (item[1], item[0]))