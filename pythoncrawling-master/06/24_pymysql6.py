#1.PyMySql 모듈을 import 
import pymysql
 
#2.MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='mydb', charset='utf8')
 
#3.Connection 으로부터 Cursor 생성  
curs = conn.cursor()
 
#4.SQL문 실행
sql = """DELETE FROM movie 
        WHERE id = %s """

curs.execute(sql, 10)
 
#5.Commit하지 않으면, 테이블의 데이타는 변경되지 않는다는 점
conn.commit()    # 전체 rows =>튜플 


#결과 확인
sql = "select * from movie"
curs.execute(sql)

rows = curs.fetchall()
print(rows)     # 전체 rows =>튜플 

for row in rows :
    for item in row :
        print(item, end=" ")
    print()


#6.Connection 닫기
conn.close()



