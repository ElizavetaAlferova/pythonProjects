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
print(st1)
print(st2)
print(st3)
print(st4)
print()
print('Частота встречаемости букв в каждом из четырех массивов: ')
print(c(st1))
print(c(st2))
print(c(st3))
print(c(st4))






