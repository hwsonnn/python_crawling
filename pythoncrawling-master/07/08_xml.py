from urlToStr import urlToStr
from bs4 import BeautifulSoup
from datetime import date, time, datetime, timedelta

def xmlparse(data) :
    bs = BeautifulSoup(data, "lxml-xml")
    dailyBoxOfficeList = bs.find_all("dailyBoxOffice")
    for dailyBoxOffice in dailyBoxOfficeList :
        rank = dailyBoxOffice.find("rank").text 
        movieNm = dailyBoxOffice.find("movieNm").text 
        rankInten = int(dailyBoxOffice.find("rankInten").text )
        
        print(rank, "위 ", end="")
        if rankInten > 0 :
            print("( ▲", end="")
        elif rankInten == 0 :
            print("( ", end="")
        else:
            print("( ▼", end="")
        
        print(str(abs(rankInten)),") ", end="")
        print(movieNm)

def viewDate() :
    ctime = datetime.now() - timedelta(days=1)
    ctime = ctime.strftime("%Y%m%d")

    return ctime

if __name__ == "__main__":
    ctime = viewDate()
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=430156241533f1d058c603178cc3ca0e&targetDt=" + ctime

    data = urlToStr(url)
    xmlparse(data) 