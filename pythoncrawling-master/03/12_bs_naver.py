from bs4 import BeautifulSoup
import urlToStr
import re
import matplotlib.pyplot as plt
#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

yitem=[] 
for y in range(1,6) :
    url = "https://movie.naver.com/movie/point/af/list.nhn?&page=" + str(y)
    html = urlToStr.urlToStr(url)
    print(url)

    bs = BeautifulSoup(html, "html.parser")
    body = bs.body  
    movies = body.select("tbody > tr")
    #print(movies)
    for movie in movies:
        star = float(movie.find("em").text)
        yitem.append(star) 

print(yitem)
print("평점 총점: ", end="")
print(sum(yitem) /len(yitem))

plt.plot(yitem) 
plt.title("최신 50 평점")
plt.show()