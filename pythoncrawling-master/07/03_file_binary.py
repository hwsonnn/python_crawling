f = open("01_htm.html", "r", encoding="utf-8")
data = f.read()
f.close()

# print(data)
# print("-"*30)

# f = open("03_htm.html", "w", encoding="utf-8")
# f.write(data)
# f.close()

f = open("03.html", "wb")
f.write(data.encode())
f.close()

f = open("03.html", "rb")
data2 = f.read()
f.close()

print(data2)
print("-"*30)
print(type(data2))
data3 = data2.decode("utf-8")
print(data3)
print(type(data3))

# print(data)
