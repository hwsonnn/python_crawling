from fileToStr import fileToStr
from datetime import datetime
import re

data = fileToStr("01_htm.html")
print(data)

#https://www.gnu.org/graphics/logo-fsf.org-tiny.png
imgsrc = re.search(r'href=["\']?([\w\d:/\.-]+)', data)
print(imgsrc.group(1))