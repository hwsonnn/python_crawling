from bs4 import BeautifulSoup
import urlToStr
import re
import matplotlib.pyplot as plt
#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

sy = int(input("시작년도입력(yyyy)"))
fy = int(input("종료년도입력(yyyy)"))

if sy > fy :
    temp = sy
    sy = fy
    fy = temp

yitem=[]
ylabel=[]
for y in range(fy, sy-1, -1) :
    url = "https://movie.daum.net/boxoffice/yearly?year=" + str(y)
    html = urlToStr.urlToStr(url)

    ylabel.append(y)
    bs = BeautifulSoup(html, "html.parser")
    body = bs.body 
    print(url)
    wrap_movies = body.select("#mArticle li")
    num =0
    listMovie = []
    for wrap_movie in wrap_movies:
        st_movie = str(wrap_movie)
        
        if len(st_movie) > 100 : 
            grade =  float(wrap_movie.select_one(".emph_grade").text)
            listMovie.append(grade)

    yitem.append(listMovie)

for i in range(len(yitem)) :
    print(yitem[i])
    print(ylabel[i])
    print("-"*20)    

x = [i+1 for i in range(len(yitem[0]))]
#print(x)
for i in range(len(yitem)):
    plt.plot(x,yitem[i], label=ylabel[i])

plt.legend()
plt.title("년도별 순위 평점")
plt.show()