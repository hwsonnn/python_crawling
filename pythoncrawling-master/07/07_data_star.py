from urlToStr import urlToStr
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def star(data):
    bs = BeautifulSoup(data,"html.parser")
    
    lis = bs.select("#mArticle ul li")
    ranklist = []
    for li in lis :
        taga = li.select_one(".desc_boxthumb")
        if taga : 
            rank = float(taga.select_one(".emph_grade").text)
            ranklist.append(rank)

    return ranklist

if __name__ == "__main__" :
    s = int(input("시작년도입력"))
    f = int(input("종료년도입력"))

    if s > f :
        temp = s 
        s = f
        f = temp

    print("시작=>", str(s), "종료=>", str(f))

    labels = []
    ylist = []
    for y in range(s, f+1) : 
        url = "https://movie.daum.net/boxoffice/yearly?year=" + str(y)
        print(url)
        data = urlToStr(url)
        ranklist = star(data)
        ylist.append(ranklist)
        labels.append(y)

    for i in range(len(ylist)) :
        plt.plot(ylist[i], label=labels[i])
    
    plt.legend()
    plt.show()