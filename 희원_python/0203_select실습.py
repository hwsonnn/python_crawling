from urlToStr2 import urlToStr
from bs4 import BeautifulSoup

data=urlToStr("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

bs = BeautifulSoup(data, "html.parser")

tit3s=bs.select("tbody>tr")
#for tit3 in tit3s :
    #tit3_tags = tit3.find_all("td")
    #if (len(tit3_tags)==4) :
        #for td in tit3_tags:
            #print(td)
            #print("-"*10)           
    #print("-"*30)
                            #각 td태그의 속성들을 보고싶음


for tit3 in tit3s :
    tit3_tags = tit3.find_all("td")
    if (len(tit3_tags)==4) :
        if tit3_tags[0].find("img") :
            #32,49위에 image가 없음. image가 있으면 가져온다.
           print(tit3_tags[0].find("img").get("alt"))
        print(tit3_tags[1].find("a").text)
        print(tit3_tags[2].find("img")['src'])
        print(tit3_tags[3].text)
    print("-"*30)


#html 계층구조 tag list 
