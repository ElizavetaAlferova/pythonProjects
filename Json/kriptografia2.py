import sys
from collections import OrderedDict
def c(a):
    d1=OrderedDict()
    for i in a:
        d1[i] = d1.get(i, 0) + 1
    let="АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
    for i in let:
        if i not in d1:
            d1[i]=d1.get(i, 0)
    sorted_t1 = OrderedDict(sorted(d1.items(), key=lambda item: item))
    sorted_t1.move_to_end('_', last=True)
    return list(dict(sorted_t1).values())
def indexes(s2):
    inds=[]
    list2 = [s2]
    for j in range(32):
        s2 = s2[-1:] + s2[:-1]
        list2.append(s2)
    for i in list2:
        print(i)
    print()
    for i in list2:
        op = 0
        for j in range(len(s1)):
            op += ((s1[j] * i[j]) / (len(st1) * len(st2)))
        inds.append(op)

    return max(inds)
data = input()
st1=[]
st2=[]
st3=[]
st4=[]
for i in range(1, len(data)+1):
    if i%4==1:
        st1.append(data[i-1])
    elif i%4==2:
        st2.append(data[i-1])
    elif i%4==3:
        st3.append(data[i-1])
    elif i%4==0:
        st4.append(data[i-1])
s1=c(st1)
s2 = c(st2)
s3 = c(st3)
s4=c(st4)
print(indexes(s2))
print(indexes(s3))
print(indexes(s4))







