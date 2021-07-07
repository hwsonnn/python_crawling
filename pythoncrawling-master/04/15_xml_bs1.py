from urlToStr import urlToStr
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date
import re

xmldata = urlToStr("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2641060000")

#bs = BeautifulSoup(xmldata, "html.parser")
bs = BeautifulSoup(xmldata, "lxml-xml")

pubDate = bs.find("pubDate").text
y = int(re.search(r'([\d]+)년', pubDate).group(1))
m = int(re.search(r'([\d]+)월', pubDate).group(1))
d = int(re.search(r'([\d]+)일', pubDate).group(1))
h = int(re.search(r'([\d]+):([\d]+)', pubDate).group(1))
s = int(re.search(r'([\d]+):([\d]+)', pubDate).group(2))
dt = datetime(y,m,d, h, s)
ddt = date(y,m,d)
print(dt, "일자")

# dt2 = ddt + timedelta(days=2)
# print(dt2)

datas = bs.find_all("data")
for data in datas: 
    dspDate = ddt + timedelta(days=int(data.find("day").text))
    print(datetime.strftime(dspDate, "%Y").strip(), "년 ", end="")
    print(datetime.strftime(dspDate, "%m").strip(), "월 ", end="")
    print(datetime.strftime(dspDate, "%d").strip(), "일 ", end="")
    print(" : ", data.find("hour").text , "시 (",  data.find("wfKor").text , ")")