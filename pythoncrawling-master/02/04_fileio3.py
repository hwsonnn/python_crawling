#파일 열기
f = open("01_html_css.html", "r", encoding="utf-8")
data = f.read()
#파일 종료
f.close()

#데이터 객체 사용
#print(data)

#문자열 슬라이싱
#print(data[0:15])

checkHtml = data[0:15]
print(checkHtml)

""" 
for item in checkHtml:
    print(item)
 """

checkHtml2 = checkHtml.replace("<", "").replace(">","")
print(checkHtml2)
print(checkHtml2.count("html"))
print(checkHtml2.find("html"))
print(checkHtml2.index("html"))
print("html" in checkHtml2)

checkHtml3 = checkHtml2.split(" ")
print(checkHtml3)