from urlToStr import urlToStr 
from datetime import datetime, timedelta, date
import json 

dt = datetime.now() - timedelta(days=1) 
dt = datetime.strftime(dt, "%Y%m%d")
 
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=" + dt
data = urlToStr(url)

dicdata = json.loads(data)

#print(dicdata)
dailyBoxOfficeList = dicdata.get("boxOfficeResult").get("dailyBoxOfficeList")
for dailyBoxOffice in dailyBoxOfficeList :
    ans = dailyBoxOffice.get("rank") + "위 (" 
    rankInten = int(int(dailyBoxOffice.get("rankInten")))

    if rankInten > 0 : ans = ans + "▲" 
    elif rankInten < 0 : ans = ans + "▼"

    ans = ans + str(abs(rankInten)) + ") "
    ans = ans + dailyBoxOffice.get("movieNm")
    print(ans)

