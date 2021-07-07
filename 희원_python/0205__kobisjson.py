from urlToStr2 import urlToStr
from filetostr import fileToStr
from bs4 import BeautifulSoup
import json

from datetime import date, time, datetime, timedelta
print(datetime)
ctime = datetime.now() - timedelta(days=1)
ctime = str(ctime.strftime('%Y%m%d'))


def jsonparser(dataj) :
    dailyBoxOfficeList = dataj.get('boxOfficeResult').get('dailyBoxOfficeList')
    #print(dailyBoxOfficeList)
    for dailyBoxOffice in dailyBoxOfficeList :
        ans = dailyBoxOffice.get("rank") + "위 (" 
        rankInten = int(int(dailyBoxOffice.get("rankInten")))

        if rankInten > 0 : ans = ans + "▲" 
        elif rankInten < 0 : ans = ans + "▼"

        ans = ans + str(abs(rankInten)) + ") "
        ans = ans + dailyBoxOffice.get("movieNm")
        print(ans)


if __name__=='__main__' :
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=" + ctime

    # print(ctime)
    data = urlToStr(url)
    dataj = json.loads(data)
    jsonparser(dataj)
    #print(dataj)


