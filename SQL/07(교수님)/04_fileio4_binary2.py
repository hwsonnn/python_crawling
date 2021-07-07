#text 파일 읽기
f = open("01_html_css.html", "r", encoding="utf-8")
data = f.read()
f.close()

# #binary 파일 쓰기
# f = open("01_html_css_b.html", "wb")
# f.write(data.encode())
# f.close()

# #binary 파일 읽기 
# f = open("01_html_css_b.html", "rb")
# data = f.read()
# f.close()

# print(data)
# print(data.decode("ascii", errors="replace")) 


