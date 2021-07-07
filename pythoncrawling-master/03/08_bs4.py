from bs4 import BeautifulSoup
import func
import re

html = func.fileToStr("01_html_css.html")

bs = BeautifulSoup(html, "html.parser")

#태그 가져오기
body = bs.body 
 
#select 가져오기
img = body.select_one("img[src]")
print(img)
print("-"*20)

imgsrc = re.search(r'src=["\']?([\w://./-]+)', str(img)).group(1)

print(imgsrc)
print("-"*20)

