from urlToStr import urlToStr
from xml.etree import ElementTree 

xmldata = urlToStr("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2641060000")

#fromstring() : 문자열로 된 XML 데이터를 받아 들일때 사용
et = ElementTree.fromstring(xmldata)
print(et)

pubDate = et.find("channel/pubDate")
print(pubDate.text)

pubDate = et.findtext("channel/pubDate")
print(pubDate)

pubDate = et.findall("channel/pubDate")
print(pubDate[0].text)

pubDate = et.find("channel").find("pubDate")
print(pubDate.text)