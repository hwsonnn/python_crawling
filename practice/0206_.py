import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='testdb', charset='utf8')

curs = conn.cursor()

#sql = "insert into codes values ('0105018','test','')"
#sql = "update codes set korNm = '금정구' where fullCd='0105018'"
sql = "delete from codes where fullCd='0105018'"

curs.execute(sql)   

conn.commit()            

conn.close()
                