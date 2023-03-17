

a, b, c = [int(input()) for i in range(3)]
if c<0 or a==0 and c**2-b!=0:
    print('NO SOLUTION')
elif a==0 and b==c**2:
    print('MANY SOLUTIONS')

else:
    s = (c**2-b)/a
    if int(s)!=s:
        print('NO SOLUTION')
    else:
        print(int(s))


