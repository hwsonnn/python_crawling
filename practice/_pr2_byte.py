s="test"
print(type(s))
print("-"*20)

bs=s.encode() #바이트 문자열로 인코딩
print(bs)
print(type(bs))
print("-"*20)

sd=bs.decode("ascii") #우리가 읽을 수 있도록 디코딩
print(sd)
##  ascii문자에는 한글이 없음
#   -> utf-8 사용
# 예시
# a="안녕하세요"
# ba=a.encode()
# ad=ba.decode("utf-8")
# print(ad)