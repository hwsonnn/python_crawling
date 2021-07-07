from urllib.request import urlopen
import re

def urlCharset(data1024) :
    encoding= re.search(r'charset=["\']?([\w\d-]+)',data1024)
    #print(data1024)
    if encoding :
        encoding= encoding.group(1)     #([\w\d-]+)를 읽어냄
    else :
        encoding="utf-8"    #meta 태그 안에 charset이 없을 경우 'utf-8'로 읽을 것
                            #앞으로 공공데이터를 가져올건데 xml파일 등도 다 읽어올 수 있게 하기 위함.        
    return encoding


def urlToStr(url) :
    rs=urlopen(url)
    data=rs.read()          #바이트 문자열이 그대로 넘어옴 -> str로 바꿔줘야 한다.
    encoding = urlCharset(data[:1024].decode("ascii",errors="replace"))
                                            #ascii가 제일 낫다고 했음 ascii코드를 쓰고 한글이 나오면 뭉갠다
    data=data.decode(encoding, errors="ignore")
    return data

if __name__ == "__main__" :         #이 파일에서만 사용되는 메인 구문
    url = input("주소를 입력하세요.")
    data=urlToStr(url)

    print(data)
