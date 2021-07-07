# from urllib.request import urlopen

# rs=urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
# data=rs.read()
# print(data)   #decoding 안한 상태


#pip install bs4
from urlToStr2 import urlToStr
from bs4 import BeautifulSoup

data=urlToStr("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
#print(data) #decoding 시켜줌
             #우리가 읽을 수 있는 상태
             #개발자 도구 그대로 읽힘
            
bs=BeautifulSoup(data,"html.parser")
#html 형식임을 알려줌(그렇게 읽을 수 있도록)

# url 불러와서 필요한 tag 읽기
# meta=bs.meta
# print(meta)
# div=bs.div
# print(div)
# a=bs.a
# print(a)
p=bs.p
print(p)
print(type(p))
print("-"*30)

p1=bs.find("p")
#print(p1) == pirnt(p)
print(p1.text)
print(type(p1))
print("-"*30)

ps=bs.find_all("p")
print(ps)
print(type(ps)) #list --> for문 사용 가능
print("-"*30)

for p in ps :
    # print(p)
    # print("*"*30)
    print(p.text)   #tag 제거
    print("*"*30)

