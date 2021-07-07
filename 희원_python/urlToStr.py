from urllib.request import urlopen

def urlToStr(url) :
    rs=urlopen(url)
    data=rs.read()

    data=data.decode("utf-8")
    return data

if __name__ == "__main__" :
    url = input("주소를 입력하세요.")
    data=urlToStr(url)

    #print(type(data))  보면 바이트 문자열로 출력. 문자열로 출력하고 싶음!
                #-----> decoding
    print(data)

#네이버영화홈은 실행이 되는데, 네이버영화랭킹페이지는 실행이 안됨.
#페이지 소스를 보면 euc-kr로 되어있음
#즉, euc-kr로 디코딩을 해야한다.

#->urlToStr2.py



    
