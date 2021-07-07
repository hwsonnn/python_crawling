#실습
import re

import filetostr as fts
data = fts.fileToStr("01_htm.html")

print(data)

imgsrc=re.search(r'href=["\']?[\w\d-]+',data)

#미완성