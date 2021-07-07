import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='testdb', charset='utf8')

#Dictoionary Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from codes"                 
curs.execute(sql)               

rows = curs.fetchall()
print(rows)      # 전체 rows =>딕셔너리   

for row in rows :
    print(row['fullCd']," ",row['korNm'])
conn.close()
                