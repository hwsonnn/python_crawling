from bs4 import BeautifulSoup
import func

html = func.fileToStr("01_html_css.html")

bs = BeautifulSoup(html, "html.parser")

#메타 태그 가져오기
meta = bs.meta 
print(meta)
print(type(meta))
 