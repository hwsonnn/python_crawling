# f=open("01_htm.html","r",encoding="utf-8")
# data=f.readline()   #첫번째문장
# f.close()

# print(data)
# print("-"*30)

# f2=open("01_htm.html","r",encoding="utf-8")
# data2=f2.readlines()    #줄단위로 끊어서
# f2.close()

# print(data2)
# print("-"*30)

f3=open("01_htm.html","r",encoding="utf-8")
data3=f3.read()     #코딩 자체를 그대로
f3.close()

# print(data3)
# print("-"*30)
print(type(data3))

f4=open("01_htm.html","rb") #Byte 문자
data4=f4.read()
f4.close()

# print(data4)
# print("-"*30)
print(type(data4))
#print(data4.decode("utf-8"))


# data=data.replace("\n","").replace("<","").replace(">","").replace("!","")
# print(data)
# print("-"*30)

# for c in data:
#     if c != " " : print(c)
#     else : print("*"*20)
# print("문자열길이 :" , len(data))
# print("문자열길이 : " + str(len(data)))


# words=data.split(" ")
# print(words)
# print("-"*30)

# for word in words:
#     if "t" in word.lower():print(word)
#     else:print("*"*20)




