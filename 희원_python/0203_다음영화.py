from urlToStr2 import urlToStr
from bs4 import BeautifulSoup

data=urlToStr("https://movie.daum.net/boxoffice/yearly?year=2017")

bs = BeautifulSoup(data, "html.parser")

#print(data)

lis=bs.select("#mArticle ul li")

#print(lis)

n=0
for li in lis :
    taga=li.select_one(".desc_boxthumb a")
    # print(taga)
    if taga :
        n=n+1
        print(n, "위", taga.text)

    if n==10 : break

