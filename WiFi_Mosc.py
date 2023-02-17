import csv

with open('D:\\Downloads\wifi.csv', encoding="utf-8") as file:
    rows = csv.DictReader(file, delimiter =";")
    dict_dist_num={}
    for row in rows:
        dict_dist_num[row["district"]]=dict_dist_num.get(row["district"], 0)+int(row["number_of_access_points"])
    sorted_tuple=sorted(dict_dist_num.items(), key = lambda x: (-x[1], x[0]))
    for i in sorted_tuple:
        print(f"{i[0]}: {i[1]}")
    # print(dict_dist_num)
    # print(sorted_tuple)