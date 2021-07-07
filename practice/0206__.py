import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root1234',
                       db='testdb', charset='utf8')

curs = conn.cursor()

#4.SQL문 실행
data = (
    ('신과함께-죄와 벌', 5, 'http://t1.daumcdn.net/movie/ff9d430c0d2df2a1c659ccba8b621ad2251f6f02', 7.0, '2017.12.20', 2018),
    ('쥬라기 월드: 폴른 킹덤', 6, 'http://t1.daumcdn.net/movie/d9b4fd04ea18b4db74f3ddfc9ebc3c22e8a0cd1b', 7.1, '2018.06.06', 2018),
    ('앤트맨과 와스프', 7, 'http://t1.daumcdn.net/movie/f60e1438ee6ca99476e393258c41e11bf6e28138', 7.4, '2018.07.04', 2018),
    ('안시성', 8, 'http://t1.daumcdn.net/movie/8d6743476fdf438e846ccab9ac59b1491537322852509', 7.6, '2018.09.19', 2018)
)
sql = """INSERT INTO movie (mtitle, rank, imgurl, star, cdate, cyy) 
        values 
        (%s, %s, %s, %s,%s,%s)"""

curs.executemany(sql, data)

#5.Commit하지 않으면, 테이블의 데이터는 변경되지 않는다는 점
conn.commit()    # 전체 rows =>튜플            

conn.close()
                