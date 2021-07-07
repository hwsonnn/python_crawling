s = "안녕하세요"
print(type(s))

print("-"*20)
bs = s.encode()
print(bs)
print(type(bs))

sd = bs.decode("ascii", errors="replace")
print(sd)
sd = bs.decode("utf-8")
print(sd)