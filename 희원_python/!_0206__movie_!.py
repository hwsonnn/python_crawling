#실습
# 네이버 최신 1000건의 평점 데이터를 그롤링하여
# 테이블을 만들고 리뷰수가 10회 이상이면서
# 평점이 8 이상인 영화를 추천하시오


from urlToStr2 import urlToStr
from bs4 import BeautifulSoup

def naverCraw(page) :
    data=urlToStr("https://movie.naver.com/movie/point/af/list.nhn?&page="+page)

    bs = BeautifulSoup(data, "html.parser")

    tit3s=bs.select("tbody>tr")

    cnt=0
    datars=[]
    for tit3 in tit3s :
        cnt=cnt+1
        datars1=[]
        mvname = tit3.find("a").text
        star = int(tit3.find("em").text)
        writer = tit3.select_one(".author").text
        cdate = tit3.find_all("td")[2].text.split("****")[1]
        datars1.append(mvname)
        datars1.append(star)
        datars1.append(writer)
        datars1.append(cdate)
        #print(cnt, ":", mvname, star, writer, cdate)
        datars1=tuple(datars1)
        datars.append(datars1)
        #print(datars1)
        #print("-"*30)

    return datars

if __name__ == "__main__" :
    datars=naverCraw("2")
    print(datars)





                