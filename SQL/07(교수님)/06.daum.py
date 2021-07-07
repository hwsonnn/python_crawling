from urlToStr import urlToStr
from bs4 import BeautifulSoup

data = urlToStr("https://movie.daum.net/boxoffice/yearly")

#print(data)
bs = BeautifulSoup(data,"html.parser")

lis = bs.select("#mArticle ul li")
n = 0
for li in lis :
    taga = li.select_one(".desc_boxthumb > .tit_join > a")
    if taga :
        n = n + 1
        print(n ,"위", taga.text)

    if n == 10 : break    