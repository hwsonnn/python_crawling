USE mydb ;

DROP TABLE movie ;
CREATE TABLE IF NOT EXISTS movie (
id INT AUTO_INCREMENT PRIMARY KEY,
mtitle VARCHAR(20) NOT NULL,
rank INT,
imgurl VARCHAR(100),
star FLOAT,
cdate CHAR(10),
cyy INT
)


DESC movie ;

INSERT INTO movie 
(mtitle, rank, imgurl, star, cdate, cyy)
VALUES 
('스파이더맨: 홈 커밍', 4, 'http://t1.daumcdn.net/movie/4f9750f09dac0f1b3659ae03cfe9ed7938be8d30', 8.1, '2017.07.05', 2017) ;

INSERT INTO movie 
(mtitle, rank, imgurl, star, cdate, cyy)
VALUES 
('스파이더맨: 홈 커밍', 4, 'http://t1.daumcdn.net/movie/4f9750f09dac0f1b3659ae03cfe9ed7938be8d30', 8.1, '2017.07.05', 2017) ;

INSERT INTO movie 
(mtitle, rank, imgurl, star, cdate, cyy)
VALUES 
('신과함께-인과 연', 1, 'http://t1.daumcdn.net/movie/e78737f6be1573f673b561f3fc0b32a8cffce820', 6.8, '2018.08.01', 2018) ;

INSERT INTO movie 
(mtitle, rank, imgurl, star, cdate, cyy)
VALUES 
('어벤져스: 인피니티 워', 2, 'http://t1.daumcdn.net/movie/dd84b905224c91225aa2a15203aba3a354197c1d', 7.6, '2018.04.25', 2018) ;

INSERT INTO movie 
(mtitle, rank, imgurl, star, cdate, cyy)
VALUES 
('보헤미안 랩소디', 3, 'http://t1.daumcdn.net/movie/ce3cd6a875284e8b96414ef3696756a11544772388211', 9.0, '2018.10.31', 2018) ;

INSERT INTO movie 
(mtitle, rank, imgurl, star, cdate, cyy)
VALUES 
('극한직업', 1, 'http://t1.daumcdn.net/movie/4e00e81f2b6f4d2eb65b3387240cc3c01547608409838', 7.4, '2019.01.23', 2019) ;

INSERT INTO movie 
(mtitle, rank, imgurl, star, cdate, cyy)
VALUES 
('어벤져스: 엔드게임', 2, 'http://t1.daumcdn.net/movie/5574fb2c20c844629aa9ad1d6043ee851555464908641', 7.8, '2019.04.24', 2019) ;

INSER INTO movie (mtitle, rank, imgurl, star, cdate, cyy) values ('알라딘', 4, 'http://t1.daumcdn.net/movie/3673a8a0c5ff4f5c8c25cc959fd6985b1558662957684',8.4,'2019.05.23',2019)
SELECT * FROM movie ;

UPDATE movie 
SET 
mtitle = '택시운전사', 
rank = 2, 
imgurl = 'http://t1.daumcdn.net/movie/c98cf3e74671b88df0f2b31b516c0aaea2e1a816', 
strar = 9.0, 
cdate = '2017.08.02', 
cyy = 2017
WHERE  id = 1

DELETE FROM movie WHERE  id = 2


SELECT * FROM movie ;

SELECT concat(cyy), rank, mtitle 
FROM movie 
ORDER BY cyy DESC, rank ;

SELECT concat(cyy) , round(AVG(star),2) AS starAvg
FROM movie
GROUP BY cyy