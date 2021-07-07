from bs4 import BeautifulSoup
import urlToStr
import re

sy = int(input("시작년도입력(yyyy)"))
fy = int(input("종료년도입력(yyyy)"))


if sy > fy :
    temp = sy
    sy = fy
    fy = temp

for y in range(fy, sy-1, -1) :
    url = "https://movie.daum.net/boxoffice/yearly?year=" + str(y)
    html = urlToStr.urlToStr(url)

    bs = BeautifulSoup(html, "html.parser")
    body = bs.body 
    print(url)
    wrap_movies = body.select("#mArticle li")
    num =0
    for wrap_movie in wrap_movies:
        st_movie = str(wrap_movie)
        if len(st_movie) > 100 : 
            listMovie = []
            #print(wrap_movie)
            title = wrap_movie.select_one(".desc_boxthumb a").text
            listMovie.append(title)

            num = num + 1
            listMovie.append(num)

            imgsrc = re.search(r'fname=["\']?([\w\d:/.?]+)', st_movie).group(1)
            listMovie.append(imgsrc)

            grade =  float(wrap_movie.select_one(".emph_grade").text)
            listMovie.append(grade)

            dd = wrap_movie.find("dd").text[:9]  
            listMovie.append(dd)

            listMovie.append(y)
            
            print(listMovie)
            print("-"*20)
        