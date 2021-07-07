from urlToStr2 import urlToStr
from bs4 import BeautifulSoup

data=urlToStr("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

bs = BeautifulSoup(data, "html.parser")

# p1=bs.select_one("p")
# print(p1)
# print("-"*30)

# tit3=bs.select_one(".tit3")
# print(tit3)
# print("-"*30)
tit3s=bs.select(".tit3") #class=tit3
# print(tit3s)
# print("-"*30)


#영화랭킹 제목 뽑기
for tit3 in tit3s :
    print(tit3.text.replace("\n",""))
print("-"*30)

#영화랭킹 순위변동폭 뽑기
ranks=bs.select(".range.ac")
for rank in ranks :
    print(rank.text)
print("-"*30)

#제목,변동폭 같이 뽑기
movies=bs.select("tbody>tr")
for movie in movies :
    movie_tags = movie.find_all("td")
    # print(movie_tags)
    # print("-"*30)
    if(len(movie_tags)==4) :
        print(movie_tags[1].text.replace("\n",""), " : ", movie_tags[3].text)
        print("-"*30)

# 영화순위정보를 나타내는 tr들 중에 (i.e len(td)==4)
# 각 tr>td들의 속성들을 각각 따로 보고싶음
# for movie in movies :
#     movie_tags = movie.find_all("td")
#     if (len(movie_tags)==4) :
#         for td in movie_tags:
#             print(td)
#             print("-"*10)           
#     print("-"*30)