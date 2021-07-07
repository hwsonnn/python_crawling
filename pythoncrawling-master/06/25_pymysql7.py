#1.PyMySql 모듈을 import 
import pymysql
 
#2.MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='mydb', charset='utf8')
 
#3.Connection 으로부터 Cursor 생성  
try :
    with conn.cursor() as curs :       
        #4.SQL문 실행
        sql = """INSERT INTO movie (mtitle, rank, imgurl, star, cdate, cyy) 
        values 
        (%s, %s, %s, %s, %s, %s)"""

        curs.execute(sql, ('알라딘', 4, 'http://t1.daumcdn.net/movie/3673a8a0c5ff4f5c8c25cc959fd6985b1558662957684',8.4,'2019.05.23',2019))
    
    #5.Commit하지 않으면, 테이블의 데이타는 변경되지 않는다는 점
    conn.commit()    # 전체 rows =>튜플 

    #결과 확인
    with conn.cursor() as curs : 
        sql = "select * from movie"
        curs.execute(sql)

        rows = curs.fetchall()
        print(rows)     # 전체 rows =>튜플 

        for row in rows :
            for item in row :
                print(item, end=" ")
            print()

finally:
    #6.Connection 닫기
    conn.close()
    