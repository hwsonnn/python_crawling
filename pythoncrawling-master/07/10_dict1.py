#파이썬 data type
#리스트와 튜플은 순서가 정해져 있음
#리스트(list) : 리스트 수정 가능 
xl = ["1", 2, 2.5, [7,8,9]]
xl.append("안녕")
xl[0] = "2"
for x in xl :
    print(x)
print("-"*20)

#튜플(tuple) : 튜플 수정 불가
xt = ("1", 2, 2.5, [7,8,9])
#xt[0] = "2"
for x in xt :
    print(x)


#형변환 
print(type(xt))
xt = list(xt)
print(type(xt))
xt[0] = "2"
xt = tuple(xt)
print(type(xt))
for x in xt :
    print(x)

print("-"*20)
#슬라이싱 : 문자열, 리스트, 튜플 
print(xt[:3])   
print(xt[3:])  
