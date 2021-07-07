import re

#파일 열기
#f = open("binarytest.html", "rb")
f = open("01_html_css_b.html", "rb")
data = f.read()
#파일 종료
f.close()

dataEncoding = data[:1024].decode()
print(type(dataEncoding))

#정규표현식
#charset=뒤에 ",' 문자가가 없거나 하나가 있고 
#알파벳문자나 -문자가 최소 한번이상 나오는 것 
#이때 알파벳문자나 -문자는 그룹
p = re.compile('charset=["\']?([\w-]+)')
encoding = p.search(dataEncoding).group(1)

print(encoding)

#r' 접두어 : 문자열에 사용된 이스케이프 시퀀스들을 
#            이스케이프 시퀀스들이 아닌 원시 문자열로 취급
encoding=re.search(r'charset=["\']?([\w-]+)', dataEncoding).group(1)
print(encoding)



