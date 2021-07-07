from urlToStr import urlToStr
import json
from datetime import date, time, datetime, timedelta

def jsonparse(data) :
    dataj = json.loads(data)
    dailyBoxOfficeList = dataj.get("boxOfficeResult").get("dailyBoxOfficeList")
    for dailyBoxOffice in dailyBoxOfficeList :
        # print(dailyBoxOffice)
        rank = dailyBoxOffice.get("rank") 
        movieNm = dailyBoxOffice.get("movieNm") 
        rankInten = int(dailyBoxOffice.get("rankInten") )
        
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
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=" + ctime

    data = urlToStr(url)
    jsonparse(data)