/*데이터 베이스 보기 */
SHOW DATABASES ;

/*데이터 베이스 생성 */
CREATE DATABASE testdb ;

/*데이터 베이스 선택 */
USE testdb ;

/*테이블 보기 */
SHOW TABLES ;

/*테이블 생성 */
CREATE TABLE codes (
	fullcd CHAR(07) PRIMARY KEY,
	kornm VARCHAR(20) NOT NULL,
	engnm VARCHAR(20)
)


/*테이블 구조 확인 */
DESC codes ;

/*자료 입력 */
INSERT INTO codes (fullcd, kornm) VALUES ('0105001', '서울시');
INSERT INTO codes VALUES('0105002', '경기도', '');
INSERT INTO codes VALUES('0105003', '강원도', NULL);
INSERT INTO codes VALUES('0105004', '충청북도', NULL);
INSERT INTO codes VALUES('0105005', '충청남도', NULL);
INSERT INTO codes VALUES('0105006', '경상북도', NULL);
INSERT INTO codes VALUES('0105007', '경상남도', NULL);
INSERT INTO codes VALUES('0105008', '전라북도', NULL);
INSERT INTO codes VALUES('0105009', '전라남도', NULL);
INSERT INTO codes VALUES('0105010', '제주도', NULL);
INSERT INTO codes VALUES('0105011', '부산시', NULL);
INSERT INTO codes VALUES('0105012', '대구시', NULL);
INSERT INTO codes VALUES('0105013', '대전시', NULL);
INSERT INTO codes VALUES('0105014', '울산시', NULL);
INSERT INTO codes VALUES('0105015', '인천시', NULL);
INSERT INTO codes VALUES('0105016', '광주시', NULL);
INSERT INTO codes VALUES('0105017', '세종시', NULL);

/*자료 확인 */
SELECT * FROM codes;

/*자료 수정 */
UPDATE codes 
SET kornm = REPLACE(kornm, "시","광역시");

UPDATE codes
SET kornm = concat(substring(kornm, 1,2),"특별시")
WHERE fullcd = '0105001'

UPDATE codes
SET kornm = concat(substring(kornm, 1,2),"시")
WHERE fullcd = '0105017'

/*자료 삭제 */
DELETE FROM codes WHERE fullcd = '0105017' ;

/*테이블에 컬럼 추가 */
ALTER TABLE codes ADD (num FLOAT) ;

UPDATE codes
SET num = RAND()*5 ;


/*자료 확인 */
/*개수 제한 */
SELECT * 
FROM codes
LIMIT 5;

/*정렬*/
SELECT kornm, fullcd
FROM codes
ORDER BY kornm; 

SELECT kornm, num
FROM codes
ORDER BY num DESC; 

/*alias */
SELECT concat(left(fullcd, 5),"-", substring(fullcd, 6,1), '-', substring(fullcd, 7,1)) AS cd, kornm 
FROM codes; 

/*alias */
SELECT left(fullcd, 5) AS CODE1 , 
       substring(fullcd, 6,1) AS CODE2, 
		 substring(fullcd, 7,1) AS CODE3, 
		 kornm 
FROM codes
WHERE substring(fullcd, 6,1) = '1';


SELECT substring(fullcd, 6,1) AS gubun, round(AVG(num),2)
FROM  codes
GROUP BY gubun ;

SELECT substring(fullcd, 6,1) AS gubun, round(AVG(num),2) AS average
FROM  codes
GROUP BY gubun 
HAVING average > 2.8;

