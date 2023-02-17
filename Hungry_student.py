import csv

with open("D:\\Downloads\\prices.csv", encoding="utf-8") as f:
    rows = csv.DictReader(f, delimiter=';')
    data=[]
    for row in rows:
        cheapest=10000000
        l=[]
        for key, value in row.items():
            if value.isdigit() and int(value)<cheapest:
                cheapest=int(value)
                l=[row["Магазин"], key, value]
                # print(l)
        data.append(l)
        # print(row)
    # print(data)
    sorted_data=sorted(data, key = lambda x: (int(x[2]), x[1], x[0]))
    print(f'{sorted_data[0][1]}: {sorted_data[0][0]}')
    # columns = rows.fieldnames