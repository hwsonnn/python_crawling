import json 

dic = {"boxofficeType":"일별 박스오피스","showRange":"20200129~20200129"} 

print("-"*20)
for item in dic.items() :
    print(item)

print("-"*20)
for key in dic.keys() :
    print(key)

print("-"*20)
for value in dic.values() :
    print(value)

print("-"*20)
for key, value in dic.items() :
    print(key, value)    

#get()으로 찾으면 해당하는 키가 없으면 none반환
print("-"*20)
print(dic.get("boxofficeType"))
print(dic["boxofficeType"])

#딕션너리 -> JSON 문자열 
print("-"*20)
jdic = json.dumps(dic, indent=4, ensure_ascii=False)
print(jdic)
print(type(jdic))

#JSON 문자열 -> 딕션너리
print("-"*20)
dic2 = json.loads(jdic)
print(dic2)
print(type(dic2))
