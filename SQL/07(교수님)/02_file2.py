f = open("01_htm.html", "r", encoding="utf-8")
data = f.readline()
f.close()

print(data)
print("-"*30)

data = data.replace("\n", "").replace("<","").replace(">","").replace("!","")
print(data)
for c in data:
    if c != " " : print(c)
    else : print("*"*20)

print("문자열길이 :" ,len(data))
print("문자열길이 :" + str(len(data)))
idx = data.find("html")
print("html찾기 :" , idx)
idx = data.find("xml")
if idx != -1 : print("xml찾기 :" , idx)
else : print("xml단어가 없습니다.")

idx = data.index("html")
print("html찾기 :" , idx)
#idx = data.index("xml")
#print("xml찾기 :" , idx)

print("-"*30)



words = data.split(" ")
print(words) 

print("-"*30)
for word in words:
    #if word == 'html' : print(word)
    if "t" in word.lower() : print(word)
    else : print("*"*20)
    
