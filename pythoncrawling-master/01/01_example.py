from urllib.request import urlopen
from bs4 import BeautifulSoup

def request(url):
    response = urlopen(url)
    byte_data = response.read()
    text_data = byte_data
    #text_data = byte_data.decode('utf-8')
    return text_data

def select_rank(data) :
    bs = BeautifulSoup(data, 'html.parser')
    seldata = bs.select(".tit3")

    return seldata

if __name__ == "__main__" :
    url = input("주소를 입력하세요.")
    data = request(url)
    #print(data)

    seldata = select_rank(data)
    num = 0 
    for item in seldata :
        num = num + 1
        print(num , "위:", item.find("a").text)




    