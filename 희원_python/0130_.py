f = open("01_htm.html","r",encoding="utf-8")
data = f.readline()
f.close()

print(data)
print("-"*30)


f = open("01_htm.html","r",encoding="utf-8")
data = f.readlines()
f.close()

print(data)
print("-"*30)


f = open("01_htm.html","r",encoding="utf-8")
data = f.read()
f.close()

print(data)
print("-"*30)