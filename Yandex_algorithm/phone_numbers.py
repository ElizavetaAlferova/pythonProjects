n1 = input()
n1 = n1.replace('-', '')
n1 = n1.replace('(', '')
n1 = n1.replace(')', '')
n1 = n1.replace('+', '')
n1.strip('+()-')
data = [input() for i in range(3)]
for i in data:
    i = i.replace('(', '')
    i = i.replace(')', '')
    i = i.replace('-', '')
    # print(i)
    # print(n1)
    if i[0]=='+':
        i=i[1:]
    # print(i)
    if len(i)==11 and len(n1)==11:
        if i[1:]==n1[1:]:
            print('YES')
        else:
            print('NO')
    elif len(i)==11 and len(n1)==7:
        if i[4:]==n1 and i[1:4]=='495':
            print('YES')
        else:
            print('NO')
    elif len(i)==7:
        if i==n1 or i==n1[4:] and n1[1:4]=='495':
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
