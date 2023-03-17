a, b, c = [int(input()) for i in range(3)]
if a<b+c and b<a+c and c<a+b and a*b*c!=0:
    print('YES')
else:
    print('NO')