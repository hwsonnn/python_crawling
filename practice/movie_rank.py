#실습
# 네이버 최신 1000건의 평점 데이터를 그롤링하여
# 테이블을 만들고 리뷰수가 10회 이상이면서
# 평점이 8 이상인 영화를 추천하시오

# +리뷰 내용 크롤링


from urlToStr2 import urlToStr
from bs4 import BeautifulSoup
from tqdm import tqdm           #진행율 보여주는거
import pymysql



def view(review, avg) :
    conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='testdb3', charset='utf8')

    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select mvname, count(*) as cnt, avg(star) as avge "
    sql = sql + "from moviestar "
    sql = sql + "group by mvname "
    sql = sql + "having cnt > " + str(review) + " and avge >= " + str(avg) + " "
    sql = sql + "order by cnt desc"   

    curs.execute(sql)               
    rows = curs.fetchall()
    conn.close()

    for row in rows :
        print(row["mvname"], "(", row["cnt"], ") : ", row["avge"])

    

def insertData(totalData) :
    conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='testdb3', charset='utf8')
                       #데이터베이스 서버의 주소를 써주면 됨
    curs = conn.cursor()
    sql="""
        insert into moviestar(mvname,star,writename,writedate,content) 
        values (%s,%s,%s,%s,%s)
        """
    curs.executemany(sql,totalData)
    conn.commit()            
    conn.close()



def naverCraw(page) :
    data=urlToStr("https://movie.naver.com/movie/point/af/list.nhn?&page="+page)

    bs = BeautifulSoup(data, "html.parser")
    tit3s=bs.select("tbody>tr")
    cnt=0
    datars=[]

    for tit3 in tit3s :
        cnt=cnt+1
        datars1=[]
        mvname = tit3.find("a").text
        star = int(tit3.find("em").text)
        writer = tit3.select_one(".author").text
        cdate = tit3.find_all("td")[2].text.split("****")[1]
        review = tit3.find_all("td")[1].find_all("a")[1]["href"].split(",")[2].replace("'","")
        datars1.append(mvname)
        datars1.append(star)
        datars1.append(writer)
        datars1.append(cdate)
        datars1.append(review)
        #print(cnt, ". ", mvname, '★', star, writer, cdate, ":", review)
        datars1=tuple(datars1)
        datars.append(datars1)
        #print(datars1)
        #print("-"*30)

    return datars



if __name__ == "__main__" :
    # totalData=[]

    # pbar=tqdm(total=100)

    # for n in range(1,101):
    #     datars=naverCraw(str(n))
    #                                     #print(datars)
    #                                     #print("-"*30)
    #     totalData=totalData+datars
    #     pbar.update(1)


    # #print(totalData)

    # insertData(tuple(totalData))           #한글 처리!!

    review = int(input("최대 조회수를 입력하세요."))
    avg = float(input("최소 평점을 입력하세요"))
    view(review, avg)
    print()
    print("ok")


