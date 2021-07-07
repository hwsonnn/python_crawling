f=open("01_htm.html","r",encoding="utf-8")
data=f.readline()
f.close()

data = data.replace("\n","").replace("<","").replace(">","").replace("!","")

idx = data.find("html") #html이 시작되는 위치
print("html 찾기 :", idx)
idx2 = data.find("xml")
#if idx2 != -1 : print("xml 찾기 :", idx2)
#else : print("xml 단어가 없습니다.")
print("xml 찾기 :", idx2)


# from filetostr import fileToStr
# data=fileToStr("01_htm.html")
# print(data)