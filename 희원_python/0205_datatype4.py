

from filetostr import fileToStr
import json


data = fileToStr('cdg.json')
dataj = json.loads(data)


#print(data)
for key, value in dataj.items() :
    print(key, value)
print('-'*30)

for key in dataj.keys():
    print(key)
print('-'*30)



# item = dataj.get('item')[0]
# print(item)
# print(type(item))


# LWCR_ICD_SUMRY = item.get('LWCR_ICD_SUMRY')
# print(LWCR_ICD_SUMRY)
# print(type(LWCR_ICD_SUMRY))































