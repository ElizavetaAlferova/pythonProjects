import json
import sys
data = json.load(sys.stdin)
for key, value in data.items():
    if type(value)!=list:
        print(f'{key}: {value}')
    else:

        value = ', '.join(map(str, value))
        print(f'{key}: {value}')

