#pip install numpy      
#matplotlib가 바로 설치 안돼서 numpy 먼저 다운
#pip install matplotlib

from urlToStr2 import urlToStr
from bs4 import BeautifulSoup
data=urlToStr("https://movie.daum.net/boxoffice/yearly?year=2019")

#*연도별로* 영화 별점을 그래프로 보고자함
#홈페이지에 있는 1-50위까지의 영화들

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
#font_manager,rc : 한글 폰트 사용하기 위함
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


# 별점!!
def star(data) :
    bs=BeautifulSoup(data, 'html.parser')
    lis=bs.select("#mArticle ul li")
    ranklist=[] #그래프 자료 넣기 위함
    for li in lis :
        taga=li.select_one('.desc_boxthumb')
        if taga :
            rank = float(taga.select_one('.emph_grade').text)
            ranklist.append(rank)
            print(rank)

    # print(type(lis)) #list
    # print(len(lis))  #53개
    print("-"*30)

    return ranklist

if __name__=="__main__" :
    s=int(input('시작년도 입력(ex)2020 : '))
    f=int(input('종료년도 입력(ex)2020 : '))

    if s>f :
        temp=s
        s=f
        f=temp
    print('시작=>',s,',종료=>',f)


labels=[]
ylist=[]
for y in range(s,f+1) :
    url='https://movie.daum.net/boxoffice/yearly?year='+str(y)
    print(url)
    data=urlToStr(url)
    ranklist=star(data)
    ylist.append(ranklist)
    labels.append(y)

for i in range(len(ylist)) :
    plt.plot(ylist[i],label=labels[i])

plt.legend(loc='upper right') #그래프를 한번에
plt.show()

# print(ylist)
# print(labels)

#ylist 안에 연도별 ranklist가 순서대로 list 형태로 들어가있음
