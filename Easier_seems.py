import csv

def condense_csv(filename, id_name):
    with open(filename, encoding="utf-8") as f:
        rows = list(csv.reader(f))
    with open("condensed.csv", "w", encoding="utf-8", newline='') as csv_file:
        writer = csv.writer(csv_file)
        headers =[id_name]
        data=[]
        finish=[]
        for row in rows:
            if row[1] not in headers:
                headers.append(row[1])
        for row in rows:
            for header in headers:
                if row[0] not in data:
                    data.append(row[0])
                if header == row[1]:
                    data.append(row[2])
                if len(data)>=len(headers):
                    finish.append(data)
                    # print(data)
                    data=[]
        print(finish)
        writer.writerow(headers)
        writer.writerows(finish)







condense_csv("D:\\Downloads\\name_log.csv", "object")