from urlToStr2 import urlToStr
from bs4 import BeautifulSoup

data=urlToStr("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

bs = BeautifulSoup(data, "html.parser")


p1=bs.select_one("p")
print(p1)
#print(p1.text)
print("-"*20)


tit3=bs.select_one(".tit3")     #하나만
print(tit3)
print("-"*20)

tit3s=bs.select(".tit3")         #리스트
print(tit3s) 
print("-"*20)


##[영화랭킹] 제목들만 뽑기
print(type(tit3s))       #리스트 형태기 때문에 print(tits.text) 오류

for tit3 in tit3s :
    print(tit3.text.replace("\n",""))
print("-"*20)



##[영화랭킹] 순위변동폭 뽑기
r=bs.select_one(".range.ac")
rs=bs.select(".range.ac")
for r in rs :
    print(r.text)
print("-"*20)


#근데 여기서 상승,하락의 순위 변동은 어떻게 뽑는지 모르겠음


#수업 (같이 뽑음)
tit3s=bs.select("tbody>tr")

#tbody>tr>td

for tit3 in tit3s :
    tit3_tags = tit3.find_all("td")
    #print(tit3_tags)
                     #tbody안에 각각의 tr태그 안에 있는 td들

    #--> 2번째 td(영화제목), 4번째 td(순위변동폭) 을 뽑아내고자 함
    if (len(tit3_tags)==4) :
        print(tit3_tags[1].text.replace("\n",""), " : ", tit3_tags[3].text)
        print("-"*30)

