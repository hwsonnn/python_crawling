from filetostr import fileToStr
import json

data = fileToStr("cdg.json")

jdata = json.loads(data)
jitem = jdata["item"]

for item in jitem:
    for k, v in item.items():
        print(k , ":", v)

# for k, v in jdata.items() :
#     print(k,v)
# print("-"*30)

# for k in jdata.keys() :
#     print(k)
# print("-"*30)