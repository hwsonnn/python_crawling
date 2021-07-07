from urlToStr2 import urlToStr
from bs4 import BeautifulSoup
data = urlToStr('https://movie.daum.net/boxoffice/yearly?year=2019')
import matplotlib.pyplot as plt
#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


def star(data):
    bs=BeautifulSoup(data, 'html.parser')
    lis=bs.select('#mArticle ul li')
    ranklist=[] # 공백 리스트 하나 생성 ==> 그래프를 만들 자료를 넣기 위해
    for li in lis:
        taga=li.select_one('.desc_boxthumb')
        if taga:
            rank = float(taga.select_one('.emph_grade').text)
            ranklist.append(rank)
            print(rank)
            print('-'*30)

    
    print(type(lis))    # type 'list'
    print(len(lis))

    return ranklist


if __name__=="__main__":
    s = int(input('시작년도 입력(ex)2019) : '))
    f = int(input('종료년도 입력(ex)2020) : '))

    if s > f : 
        temp = s
        s = f
        f = temp
    print('시작=>', str(s), ', 종료=>', str(f))

    labels = []
    ylist = []
    for y in range(s,f+1) :
        url='https://movie.daum.net/boxoffice/yearly?year='+str(y)
        print(url)
        data=urlToStr(url)
        ranklist=star(data)
        ylist.append(ranklist)
        labels.append(y)

    for i in range(len(ylist)) :
        plt.plot(ylist[i], label=labels[i])
    
    plt.legend()
    plt.show()





































