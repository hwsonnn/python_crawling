#파일 열기
f = open("01_html_css.html", "r", encoding="utf-8")
data = f.readlines()
#파일 종료
f.close()

#데이터 객체 사용
for line in data :
    print(line)
