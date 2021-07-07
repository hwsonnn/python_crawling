f = open("01_htm.html","r",encoding="utf-8")
data = f.readline()
f.close()

#첫줄
print(data)
print("-"*30)

#불필요한 요소 제거
data = data.replace("\n","").replace("<","").replace(">","").replace("!","")
print(data)
print("-"*30)


words = data.split(" ")
print(words)
print("-"*30)
for word in words:
    #if word == 'html' : print(word)
    if "t" in word.lower() : print(word)
    else : print("*"*20)


data = data.replace("\n","").replace("<","").replace(">","").replace("!","")
print(data)
for c in data:
    if c != " " : print(c)
    else : print("*"*20)
print("문자열길이 :" , len(data))
print("문자열길이 : " + str(len(data)))

idx = data.find("html")
print("html 찾기 :", idx)
idx = data.find("xml")
if idx != -1 : print("xml 찾기 :", idx)
else : print("xml 단어가 없습니다.")

idx = data.index("html")
print("html 찾기 :", idx)
#idx = data.index("xml")
#print("xml 찾기 :", idx) 
#index를 쓰면 단어가 없을 때 오류를 냄. find를 쓰는게 더 나음 

print("-"*30)

#float
#int