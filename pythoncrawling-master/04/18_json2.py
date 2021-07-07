from func import fileToStr
import json

data = fileToStr("cdg.json")

jdata = json.loads(data)
jitem = jdata["item"]

for item in jitem:
    for k, v in item.items():
        print(k , ":", v)