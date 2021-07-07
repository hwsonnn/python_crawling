from urlToStr import urlToStr
from bs4 import BeautifulSoup

data = urlToStr("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

bs = BeautifulSoup(data,"html.parser")
tit3s = bs.select("tbody > tr")
for tit3 in tit3s:
    tit3_tags = tit3.find_all("td")
    if (len(tit3_tags) == 4):
        if tit3_tags[0].find("img") :
            print(tit3_tags[0].find("img").get("alt"))
        print(tit3_tags[1].select_one(".tit3").text)
        print(tit3_tags[2].find("img")['src'])
        print(tit3_tags[3].text)
    print("-"*30)        
