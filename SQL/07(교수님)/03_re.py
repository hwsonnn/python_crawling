import re

data = "<meta charset='utf-8'>"
m = re.search(r'charset=["\']?([\w\d-]+)', data)
#m = re.search(r'charset="', data)
#print(m)
#s , f = m.span()
#print(data[s:f].split("'")[1])

print(m.group())
print(m.group(0))
print(m.group(1))