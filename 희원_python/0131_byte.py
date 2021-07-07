s="test"
#s="안녕하세요"
print(type(s))

print("-"*20)
bs=s.encode()
print(bs)
print(type(bs))

sd=bs.decode("ascii")
#ascii문자에는 한글이 없음. decoding 시킬 때 utf-8으로 사용
#sd=bs.decode("utf-8")
#sd=bs.decode("ascii",errors="replace") 이 경우, 에러를 안띄우고 뭉개버림
print(sd)



#2019.01.31 pt.2

data=1234
print(type(data))
print("-"*20)

#정수->문자열
data=str(data)
print(type(data))
print("자리수 :",len(data))
print("마지막 :",data[-1])
print("-"*20)

#문자열->바이트문자열
data=data.encode()
print(type(data))
print(data)
print("-"*20)

#바이트문자열->decoding문자열
data=data.decode("utf-8")
print(type(data))
print(data)
print("-"*20)

#바이트문자열->문자열
data=str(data)
print(type(data))
print(data)
print("-"*20)
                    #바이너리 앞에 있는 접두어까지, 즉 그 자체가 출력됨
                    #디코딩을 해서 문자열로 만들어줘야함 

data=list(data)
print(type(data))
print(data)

#리스트->문자열
data="".join(data)
print(type(data))
print(data)

#문자열->실수
data=float(data)
print(type(data))
print(data)