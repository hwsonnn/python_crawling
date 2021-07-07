#네이버 평점 크롤링 => 데이터 베이스에 저장
#old_content > table > tbody > tr:nth-child(1)
from urlToStr import urlToStr
from bs4 import BeautifulSoup
from tqdm import tqdm
import pymysql

def view(review, avg) :
    conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='testdb', charset='utf8') 
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT mvname, COUNT(*) AS cnt, AVG(star) AS avge "
    sql = sql + "FROM moviestar " 
    sql = sql + "GROUP BY mvname "
    sql = sql + "HAVING cnt > " + str(review) + " AND avge >= " + str(avg) + " "
    sql = sql + "ORDER BY avge DESC  "
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    for row in rows :
        print(row["mvname"] , "(" , row["cnt"], ") : " , row["avge"])


def insertData(totalData):
    conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='testdb', charset='utf8') 
    curs = conn.cursor()
    sql = """
            insert into moviestar(mvname, star, writename, writedate, content) 
            values (%s,%s,%s,%s,%s)
        """
    curs.executemany(sql, totalData)
    conn.commit() 
    conn.close()

def naverCraw(page) :
    data = urlToStr("https://movie.naver.com/movie/point/af/list.nhn?&page="+page)

    bs = BeautifulSoup(data,"html.parser")
    tit3s = bs.select("tbody > tr")
    cnt = 0
    datars = []
    for tit3 in tit3s:
        cnt = cnt + 1
        datars1 = []
        mvname = tit3.find("a").text
        star = int(tit3.find("em").text)
        writer = tit3.select_one(".author").text
        #old_content > table > tbody > tr:nth-child(3) > td.title > div
        content = tit3.find_all("td")[1].find_all("a")[1]["href"].split(",")[2].replace("'","")
        cdate = tit3.find_all("td")[2].text.split("****")[1]
        datars1.append(mvname)
        datars1.append(star)
        datars1.append(writer)
        datars1.append(cdate)
        datars1.append(content)
        #print(cnt , ":", mvname, star, writer, cdate, content)
        datars1 = tuple(datars1)
        datars.append(datars1)
        #print(datars1)
        #print("-"*30)    

    return datars 

if __name__ == "__main__" :
    # totalData = []

    # pbar = tqdm(total=100)
    # for i in range(1,101):
    #     datars = naverCraw(str(i))
    #     #print(datars)
    #     #print("-"*30)
    #     totalData = totalData + datars
    #     pbar.update(1)

    # insertData(tuple(totalData)) 
    review = int(input("최소 조회수를 입력하세요."))
    avg = float(input("최소100 평점을 입력하세요."))
    view(review, avg)
    print()
    print("ok")
