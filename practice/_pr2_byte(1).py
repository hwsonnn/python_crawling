data=1234
print(type(data))
print("-"*20)
#int

data=str(data) #정수 -> 문자열
print(type(data)) 
# print("자리수 :",len(data)) #4
# print("마지막 :",data[-1]) #4
print("-"*20)

data=data.encode() #문자열 -> byte문자열
print(type(data))
print(data)
print("-"*20)

data=data.decode("utf-8") #byte -> decoding문자열
print(type(data)) #str
print(data)
print("-"*20)
#   or
#data=data.encode()
#data=str(data)  #byte -> 문자열(str)
#print(type(data))
#print(data) #접두어(b' ')까지 그대로 출력
         #so, by decoding, change to str


data=list(data) #list
print(type(data))
print(data)
print("-"*20)

data="".join(data) #list -> 문자열(str)
print(type(data))
print(data)
print("-"*20)

data=float(data) #문자열(str) -> 실수
print(type(data))
print(data)
print("-"*20)


