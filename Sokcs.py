import sys
from datetime import datetime
data = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]
asc = sorted(data)
desc = sorted(data, reverse=True)
if len(data)!=len(set(data)) or data!=asc and data!=desc:
    print("MIX")
elif data==asc:
    print("ASC")
else:
    print("DESC")








