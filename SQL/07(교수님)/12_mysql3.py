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
#sql = "insert into codes values ('0105018','test','')"
#sql = "update codes set korNm = '금정구' where fullCd = '0105018'"
#sql = "delete from codes where fullCd = '0105018'"
#curs.execute(sql)

data = (('0105020', 't1', ''),('0105021', 't2', ''),('0105022', 't3', ''))
sql = "insert into codes values (%s,%s,%s)"
curs.executemany(sql, data)
conn.commit() 

#5.데이타를 서버로부터 가져온 후, Fetch 된 데이타를 사용

#6.Connection 닫기
conn.close()
