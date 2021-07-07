from urlToStr2 import urlToStr
from bs4 import BeautifulSoup

data=urlToStr("https://movie.daum.net/boxoffice/yearly?year=2019")

bs = BeautifulSoup(data, "html.parser")

#영화순위,영화제목

lis=bs.select("#mArticle ul li")
#print(lis)

n=0
for li in lis :
    movie_tag = li.select_one(".desc_boxthumb a")
    if movie_tag :
        n=n+1
        print(n,"위",movie_tag.text)
    if n==10 : break