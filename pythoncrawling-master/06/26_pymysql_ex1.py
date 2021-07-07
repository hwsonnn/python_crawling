import pymysql
from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from urlToStr import urlToStr 
import re

def dbcon() :
    #2.MySQL Connection 연결
    conn = pymysql.connect(host='localhost', user='root', password='root1234',
                        db='mydb', charset='utf8')
    
    return conn

def dbclose(conn) :
    conn.close()

def dbinsert(conn, indata) :
    curs = conn.cursor()
    sql = """DELETE FROM moviestar """

    curs.execute(sql)
    conn.commit() 

    sql = """INSERT INTO moviestar (writename, mvname, star, content,writedate) 
        values 
        (%s, %s, %s, %s, %s)"""

    curs.executemany(sql, indata)
    
    #5.Commit하지 않으면, 테이블의 데이타는 변경되지 않는다는 점
    conn.commit()    # 전체 rows =>튜플 

def recommend(conn) :
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    sql = """SELECT mvname, COUNT(*) AS cnt, AVG(star) AS staravg
            FROM moviestar 
            GROUP BY mvname
            HAVING cnt  >= 10 AND staravg > 8
            ORDER BY cnt DESC
    """
    curs.execute(sql)
    
    rows = curs.fetchall()
    # print(rows)     
    for row in rows :
        for key, value in row.items() :
            print(row[key], end=" ")
        print()

def select_rank(data) :
    bs = BeautifulSoup(data, 'html.parser')
    trdata = bs.select("tbody > tr")

    for tr in trdata:
        trlist = []
        tds = tr.find_all("td")
        writename = tds[2].find("a").text
        mvname = tds[1].select_one(".movie.color_b").text
        star = tds[1].find("em").text
        href = tds[1].select_one(".report").get("href").split(",") 
        content = href[2].replace("'", "")
        writedate = tds[2].text[-8:]
        #print(writename, mvname, content,writedate)
        trlist.append(writename)
        trlist.append(mvname)
        trlist.append(star)
        trlist.append(content)
        trlist.append(writedate)
    
        data1000.append(tuple(trlist))
    


if __name__ == "__main__" :
    data1000 = [] 
    for n in range(1,21):
        url = "https://movie.naver.com/movie/point/af/list.nhn?&page=" + str(n)
        data = urlToStr(url)
        select_rank(data)
        print(n)
    
    data1000 = tuple(data1000)
    conn = dbcon()
    dbinsert(conn, data1000)
    recommend(conn)