import re

s = 'please treate this as URGENT and important'

res = re.search(r'URGENT', s)

s = 'please treate this as URGENT and important'
res = re.search(r'URGENT', s)

print(res.group() if res else 'No match found')