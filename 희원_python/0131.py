f = open("01_htm.html","r",encoding="utf-8")
data = f.read()
f.close()

print(data)
print("-"*30)


# f = open("01_htm.html","w",encoding="utf-8")
# f.write(data)
# f.close()


# f = open("01_htm.html","wb")
# f.write(data.encode())
# f.close()


f = open("01_htm.html","rb")
data2 = f.read()
f.close()

print(data2)
print("-"*30)
print(type(data2))              #바이트 문자열
print(data2.decode("utf-8"))

#print(data)

#위 코드가 맞는지 모르겠음(data2를 뭐어떻게 읽어낸다는데)
