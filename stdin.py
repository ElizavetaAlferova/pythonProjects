import sys
from datetime import datetime, timedelta

data=sorted([datetime.strptime(line.strip(), "%Y-%m-%d") for line in sys.stdin])
print((data[-1]-data[0]).days)
