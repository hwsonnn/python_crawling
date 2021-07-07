import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='testdb', charset='utf8')

curs = conn.cursor()

sql = "select * from codes"                 
curs.execute(sql)               

rows = curs.fetchall()
print(rows)         

for row in rows :
    for item in row :
        print(item, end=" ")
    print()
    #print(row[0][:2],"-",row[0][2:4],"-",row[0][4:],' ',row[1] , sep='')

conn.close()
                