CREATE DATABASE testdb3;

USE testdb3;

CREATE TABLE if NOT EXISTS moviestar (
	id INT AUTO_INCREMENT PRIMARY KEY,
	writename VARCHAR(20),
	mvname VARCHAR(100),
	star INT,
	content TEXT,
	writedate CHAR(10)
	
);


SHOW TABLES;
DESC moviestar;

SELECT * FROM moviestar;


#원하는 내용 추출
SELECT mvname, COUNT(*) AS cnt, AVG(star) AS avge
FROM moviestar
GROUP BY mvname
HAVING cnt > 10 AND avge >= 8
						#group by 된 것은 where 쓸 수 없음
ORDER BY cnt DESC
;


SELECT * FROM moviestar
WHERE mvname = "클로젯"
;

