#파이썬 data type
#딕션너리(dict) :키와 값의 쌍
#순서가 정해져 있지 않음 

from fileToStr import fileToStr 
import json

data = fileToStr("cdg.json")
dataj = json.loads(data)

#print(data)
# for key in dataj.keys():
#     print(key)
# print("-"*30)

# for key, value in dataj.items() :
#     print(key, value)


item = dataj.get("item")[0]
print(type(item))
LWCR_ICD_SUMRY = item.get('LWCR_ICD_SUMRY')
print(LWCR_ICD_SUMRY)
print(type(LWCR_ICD_SUMRY))