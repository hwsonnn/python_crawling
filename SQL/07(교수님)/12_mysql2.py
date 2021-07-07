#1.PyMySql 모듈을 import 
import pymysql

#2.MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='testdb', charset='utf8') 

#3.Connection 으로부터 Cursor 생성 => Dictoionary Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

#4.SQL문 실행
# sql = """select concat( substring(fullCd,1,2), "-", 
#                 substring(fullCd,3,2), "-",
#                 substring(fullCd,4,3)), 
#                 korNm
#                 from codes
#       """
sql = "select * from codes"
curs.execute(sql)

#5.데이타를 서버로부터 가져온 후, Fetch 된 데이타를 사용
rows = curs.fetchall()
print(rows)     # 전체 rows =>딕션너리
for row in rows :
    print(row['fullCd'], " ", row['korNm'])

#6.Connection 닫기
conn.close()
