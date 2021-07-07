#정규표현식
#파이썬 re모듈

import re

data="<meta charset='utf-8'>"
m=re.search(r'charset',data)
m2=re.search(r'charset=["\']',data)
m3=re.search(r'charset=["\']?([\w-]+)',data)
    # " 또는 ' 가 있어도 되고 없어도 되고
    #\w 또는 - 중에서 1번 이상 반복
    #이 조건과 매치되는게 있는지
# print(m3)
# print(m3.span())
# s,f = m3.span()
# print(s,f)
# print(data[s:f])

print(m3.group())
print(m3.group(0)) #위와 동일
print(m3.group(1)) #()로 묶인 첫번째 그룹
print(m3.group(2))


#pip install numpy
#pip install matplotlib #데이터 시각화
#pip install pandas     #데이터 분석