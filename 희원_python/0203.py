from urlToStr2 import urlToStr
from bs4 import BeautifulSoup

data=urlToStr("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

bs = BeautifulSoup(data, "html.parser")

meta=bs.meta
print(meta)

div=bs.div
print(div)

a=bs.a
print(a)

p=bs.p
print(p)
print(type(p))

p1=bs.find("p")
print(p1.text)
print(type(p1))
print("*"*30)

ps=bs.find_all("p")
print(ps)
print(type(ps))     #리스트로 불러옴   --> for문 사용 가능

for p in ps :
    #print(p)
    print(p.text)  #tag를 제외시키고 tag 안에 있는 글자들만 가져오는 것
                    # tag : <p></p>
    print("-"*30)
