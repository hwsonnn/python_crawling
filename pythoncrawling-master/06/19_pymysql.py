#1.PyMySql 모듈을 import 
import pymysql
 
#2.MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='mydb', charset='utf8')
 
#3.Connection 으로부터 Cursor 생성 => Dictoionary Cursor 생성
curs = conn.cursor()
 
#4.SQL문 실행
sql = "select * from movie"
curs.execute(sql)
 
#5.데이타를 서버로부터 가져온 후, Fetch 된 데이타를 사용
rows = curs.fetchall()
print(rows)     # 전체 rows =>튜플 

for row in rows :
    for item in row :
        print(item, end=" ")
    print()

#6.Connection 닫기
conn.close()


