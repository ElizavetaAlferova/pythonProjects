from datetime import datetime
# change
pattern = '%d.%m.%Y'
n = int(input())
list_of_customers = []
for i in range(n):
    list_of_customers.append(datetime.strptime(input().split()[2], pattern))
# print(list_of_customers)
frequency = {}
for i in list_of_customers:
    frequency[i] = frequency.get(i, 0) + 1
# print(frequency)

new = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
common = new[0][1]
result = []
for i in frequency:
    if frequency[i] == common:
        result.append(i)

# print(new)
# print(common)
result = sorted(result)
for i in result:
    print(datetime.strftime(i, pattern))

# for i in list_of_customers:
