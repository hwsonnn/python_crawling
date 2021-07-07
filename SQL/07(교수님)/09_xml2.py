from urlToStr import urlToStr
from bs4 import BeautifulSoup
from datetime import date, time, datetime, timedelta

def xmlparse(data) :
    bs = BeautifulSoup(data, "lxml-xml")
    tm = bs.find("tm").text[:8]
    ctime = viewDate(tm)

    pubDate = bs.find("pubDate").text 
    category = bs.find("category").text 

    print(pubDate, "현재")
    print(category)

    datas = bs.find_all("data") 
    for data in datas :
        ctime2 = ctime + timedelta(days=int(data.find("day").text))
        hour = data.find("hour").text 
        wfKor = data.find("wfKor").text 

        print(ctime2 , " : ", hour , "시 ", wfKor)

def viewDate(tm) :
    ctime = date(int(tm[:4]), int(tm[4:6]), int(tm[6:]) )
    return ctime

if __name__ == "__main__": 
    url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2641060000"
    data = urlToStr(url)
    xmlparse(data) 