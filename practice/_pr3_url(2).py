from urlToStr2 import urlToStr
from bs4 import BeautifulSoup

data=urlToStr("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

bs = BeautifulSoup(data, "html.parser")

#영화순위,영화제목,순위변동,변동폭
movies=bs.select("tbody>tr")
for movie in movies :
    movie_tags = movie.find_all("td")
    if(len(movie_tags)==4) :
        #순위
        if movie_tags[0].find("img") :
            print(movie_tags[0].find("img")["alt"],"위",movie_tags[1].text.replace("\n",""),movie_tags[2].find("img")["alt"],movie_tags[3].text)
        # #영화제목
        # print(movie_tags[1].text.replace("\n",""))
        # #순위변동
        # print(movie_tags[2].find("img")["alt"])
        # #변동폭
        # print(movie_tags[3].text)
        print("-"*30)