from fileToStr import fileToStr
from datetime import datetime

data = fileToStr("01_htm.html")
lines = data.split("\n")

for line in lines:
    #print(line)
    if "charset" in line :
        metaline = line 
        break
metaword = metaline.split('"')
encoding = metaword[1]
print(encoding)
print(encoding[-1])