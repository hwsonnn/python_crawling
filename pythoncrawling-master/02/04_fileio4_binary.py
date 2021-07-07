cstr = "안녕하세요"
bstr = cstr.encode()

print("-"*20)
print(type(cstr))
print(cstr) 

print("-"*20)
print(type(bstr))
print(bstr[0])
print(str(bstr)[0])
print(bstr.decode("ascii", errors="replace"))
print(bstr.decode("utf-8"))

