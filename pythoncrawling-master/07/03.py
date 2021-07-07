data = 1234
print(type(data))
print("-"*20)

#정수->문자열 
data = str(data)
print(type(data))
print("자리수:", len(data))
print("마지막:", data[-1])
print("-"*20)

#문자열->바이트문자열
data = data.encode()
print(type(data))
print(data)
print("-"*20)

#바이트문자열->decoding문자열 
data = data.decode("utf-8")
print(type(data))
print(data)
print("-"*20)

#바이트문자열->문자열
# data = str(data)
# print(type(data))
# print(data)
# print("-"*20)

data = list(data)
print(type(data))
print(data)

#리스트->문자열
data = "".join(data)
print(type(data))
print(data)

#문자열->실수
data = float(data)
print(type(data))
print(data)