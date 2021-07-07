import myrequest
import xml.etree.ElementTree as ET 
from datetime import datetime, timedelta 

def dailyBoxOfficeList(data) : 
    tree  = ET.fromstring(data) # xml 문자를 이용한 파싱 
    dailyBoxOffices = tree.find("dailyBoxOfficeList").findall("dailyBoxOffice")
    #dailyBoxOffices = tree.findall("dailyBoxOfficeList/dailyBoxOffice")
     
    return dailyBoxOffices

if __name__ == "__main__" :   
    cday = datetime.now() - timedelta(days = 1)
    yyyymmdd = cday.strftime('%Y%m%d')

    print(yyyymmdd)
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=430156241533f1d058c603178cc3ca0e&targetDt=" + yyyymmdd
    data = myrequest.request(url) 
    dailyBoxOffices = dailyBoxOfficeList(data)
     
    for dailyBoxOffice in dailyBoxOffices :
        ans = dailyBoxOffice.find("rank").text + "위 (" 
        rankInten = int(int(dailyBoxOffice.find("rankInten").text))

        if rankInten > 0 : ans = ans + "▲" 
        elif rankInten < 0 : ans = ans + "▼"

        ans = ans + str(abs(rankInten)) + ") "
        ans = ans + dailyBoxOffice.find("movieNm").text

        print(ans) 