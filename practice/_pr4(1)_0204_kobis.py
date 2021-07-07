from urlToStr2 import urlToStr
from bs4 import BeautifulSoup

from datetime import date, time, datetime, timedelta
print(datetime)

#pip install lxml 
                    #실행이 안돼서 설치 후 다시 실행해서 됨
def xmlparser(dat) :
    bs = BeautifulSoup(data, 'lxml-xml')

    dailyBoxOfficeList = bs.find_all('dailyBoxOffice')
    #print(dailyBoxOfficeList)
    for dailyBoxOffice in dailyBoxOfficeList : 
        rank = dailyBoxOffice.find('rank').text
        movieNm = dailyBoxOffice.find('movieNm').text
        rankInten = int(dailyBoxOffice.find('rankInten').text)

        print(rank, '위 ', end='')
        if rankInten >0 :
            print("( ▲", end='')
        elif rankInten ==0 :
            print('(  ', end='')
        else :
            print('( ▼', end='')
        print(str(abs(rankInten)), ' )', end='')
        print(' ', movieNm)


def viewDate(tm) :
    ctime = date(int(tm[:4]), int(tm[4:6]), int(tm[6:]))
    return ctime

if __name__=='__main__' :
    ctime = datetime.now() - timedelta(days=1)
    ctime = str(ctime.strftime('%Y%m%d'))
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=430156241533f1d058c603178cc3ca0e&targetDt=" + ctime

    # print(ctime)
    data = urlToStr(url)
    xmlparser(data)


