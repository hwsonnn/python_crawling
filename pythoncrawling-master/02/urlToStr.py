from urllib.request import urlopen 
import re 

def urlCharset(data1024) :
    data1024 = data1024.decode("ascii", errors="replace")
    encoding = re.search(r'charset=["\']?([\w-]+)', data1024)

    if encoding :
        encoding = encoding.group(1)
    else :
        encoding = "utf-8"

    return encoding

def urlToStr(url) :
    resp = urlopen(url)
    data = resp.read() 

    encoding = urlCharset(data[:1024])
    dataStr = data.decode(encoding)

    return dataStr

if __name__ == "__main__" :
    url = input("url주소를 입력하세요:")
    dataStr = urlToStr(url)
    print(dataStr)
    print(type(dataStr))