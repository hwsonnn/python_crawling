#파이썬 data type
#딕션너리(dict) :키와 값의 쌍
#순서가 정해져 있지 않음 
dic = {"a": 1, "b": 2, "c": 3}

print(dic["a"])
print(dic.get("a"))
dic["d"] = 4 #추가
dic["b"] = 4 #수정
print(dic)

print("-"*20)
for item in dic :
    print(item, "=>" , dic[item])

for item in dic.items() :
    print(item)

for key, value in dic.items() :
    print(key, "=>" , value)

for key in dic.keys() :
    print(key)

for value in dic.values() :
    print(value)