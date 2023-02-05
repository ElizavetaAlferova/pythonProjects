import sys
data = [int(line) for line in sys.stdin]
dif= data[1]-data[0]
geo = data[1] // data[0]
c=0
k=0
for i in range(1, len(data)):
    if data[i]-data[i-1]!=dif:
        if data[i] // data[i-1]!=geo:
            print("Не прогрессия")
            break
    else:
        c += 1
    if data[i]// data[i-1]==geo:
       k+=1
if c+1==len(data):
    print("Арифметическая прогрессия")
if k+1==len(data):
    print("Геометрическая прогрессия")




