#파일 열기
f = open("01_html_css.html", "r", encoding="utf-8")
data = f.readline()
#파일 종료
f.close()

#데이터 객체 사용
print(data)
