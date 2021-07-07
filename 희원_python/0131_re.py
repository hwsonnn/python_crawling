#정규표현식
#파이썬 re모듈

import re

data="<meta charset='utf-8'>"
#m=re.search(r'charset',data)
#m=re.search(r'charset=["\']',data)  # =뒤에 "나 ' 중 뭐가 올 지 몰라서 둘 중 하나 오는걸로 찾고 싶음
m=re.search(r'charset=["\']?([\w\d-]+)',data) # 그것도 모르겠을 때 (둘다사용안했을수도있을때)
##data="<meta charset='euc-kr'>"
##m=re.search(r'charset=["\']?[\w\d-]+',data)

#print(m)
#print(m.span())
#s,f = m.span()
#print(s,f)
#print(data[s:f])

print(m.group())
print(m.group(0))
print(m.group(2))