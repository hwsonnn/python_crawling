#PyMySql

#1 PyMySQL 모듈 import
import pymysql

#2 MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='testdb', charset='utf8')
                #다른 SQL서버에서 불러오면 host에 그 주소를 쓰면 됨

#3 Connection으로 부터 Cursor 생성
curs = conn.cursor()

#4.SQL문 실행
sql = """select concat( substring(fullCd,1,2), "-",
                substring(fullCd,3,2), "-",
                substring(fullCd,5,3) ),
                korNm
                from codes
    """                         #명령시킬 문장 저장
curs.execute(sql)               #명령 실행

#5.데이터를 서버로부터 가져온 후, Fetch 된 데이터를 사용
rows = curs.fetchall()
print(rows)         # 전체 rows => 튜플 

for row in rows :
    print(row[0][:2],row[0][2:5],row[0][5:],' ',row[1] , sep='')

#6.Connection 닫기
conn.close()
                