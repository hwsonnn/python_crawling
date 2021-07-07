from urlToStr import urlToStr
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date

dt = datetime.now() - timedelta(days=1) 
dt = datetime.strftime(dt, "%Y%m%d")
 
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=430156241533f1d058c603178cc3ca0e&targetDt=" + dt
xmldata = urlToStr(url)

#bs = BeautifulSoup(xmldata, "html.parser")
bs = BeautifulSoup(xmldata, "lxml-xml")

datas = bs.find_all("dailyBoxOffice")
for data in datas :
    ans = data.find("rank").text + "위 (" 
    rankInten = int(int(data.find("rankInten").text))

    if rankInten > 0 : ans = ans + "▲" 
    elif rankInten < 0 : ans = ans + "▼"

    ans = ans + str(abs(rankInten)) + ") "
    ans = ans + data.find("movieNm").text

    print(ans) 
        
