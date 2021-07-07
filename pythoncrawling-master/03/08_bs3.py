from bs4 import BeautifulSoup
import func

html = func.fileToStr("01_html_css.html")

bs = BeautifulSoup(html, "html.parser")

#태그 가져오기
body = bs.body 
 
#select 가져오기
m1 = body.select_one("#m1")
print(m1)
print("-"*20)

c1 = body.select_one(".c1")
print(c1)
print("-"*20)

c1 = body.select(".c1")
print(c1)
print("-"*20)

hrefs = body.select("a[href]")
for href in hrefs:
    print(href)
print("-"*20)

hrefs = body.select("ul > li > a")
for href in hrefs:
    print(href.text)
print("-"*20)