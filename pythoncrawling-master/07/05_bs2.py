from urlToStr import urlToStr
from bs4 import BeautifulSoup

data = urlToStr("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

bs = BeautifulSoup(data,"html.parser")
# p1 = bs.select_one("p")
# print(p1.text)
# print("-"*20)

# tit3 = bs.select_one(".tit3")
# print(tit3)
# print("-"*20)

# tit3s = bs.select("tbody > tr")
# for tit3 in tit3s:
#     tit3_tags = tit3.find_all("td")
#     #print(len(tit3_tags))
#     if (len(tit3_tags) == 4):
#         print(tit3_tags[1].text.replace("\n",""), " : ", tit3_tags[3].text)
#         print("-"*30)

tit3 = bs.select(".tit3")
print(len(tit3))
ts = bs.select(".range.ac")
print(len(ts))

for i in range(len(tit3)) :
    print(tit3[i].text.replace("\n", ""), ":", ts[i].text)