from bs4 import BeautifulSoup
import func

html = func.fileToStr("01_html_css.html")

bs = BeautifulSoup(html, "html.parser")

#태그 가져오기
body = bs.body 
li = body.li
print(li)
print(type(li))
print("-"*20)

li = body.find("li")
print(li)
print(type(li))
print("-"*20)

lis = body.find_all("li")
print(lis)
print(type(lis))
print("-"*20)

for li in lis :
    print(li)
print("-"*20)

for li in lis :
    if li.find("a") : print(li.find("a"))
print("-"*20)

for li in lis :
    if li.find("a") : print(li.find("a").text)
print("-"*20)


