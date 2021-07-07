from bs4 import BeautifulSoup
import urlToStr
import re

html = urlToStr.urlToStr("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

bs = BeautifulSoup(html, "html.parser")

#태그 가져오기
body = bs.body 
 
#select 가져오기
tits = body.select(".tit3 > a")

num = 0
for tit in tits:
    num = num + 1
    print(num , "위 :" ,tit.text)

