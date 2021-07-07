from fileToStr import fileToStr
from datetime import datetime
import re

data = fileToStr("01_htm.html")
print(data)
imgsrc = re.search(r'src=["\']?(.+) ', data)
print(imgsrc.group(1).replace('"',""))