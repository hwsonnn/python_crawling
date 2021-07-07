from urlToStr import urlToStr
from bs4 import BeautifulSoup

data = urlToStr("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

bs = BeautifulSoup(data,"html.parser")
meta = bs.meta
print(meta)

a = bs.a
print(a)

p = bs.p
print(p)
print(type(p))

p1 = bs.find("p")
print(p1.text)
print(type(p1))
print("*"*30)

ps = bs.find_all("p")
print(ps)
print(type(ps))

for p in ps :
    print(p.text)
    print("-"*30)



