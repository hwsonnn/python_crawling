USE mydb ;

DROP TABLE moviestar ;
CREATE TABLE IF NOT EXISTS moviestar (
id INT AUTO_INCREMENT PRIMARY KEY,
writename VARCHAR(20),
mvname VARCHAR(100),
star int,
content TEXT,
writedate CHAR(10)
);

SELECT * FROM moviestar ;
DESC moviestar ;


SELECT mvname , AVG(star) as st , COUNT(*) as cnt 
FROM moviestar 
GROUP BY mvname 
HAVING  cnt > 20 AND st > 8
ORDER BY st DESC;

SELECT mvname, COUNT(*)
FROM moviestar
GROUP BY mvname 
ORDER BY mvname;
 ;


