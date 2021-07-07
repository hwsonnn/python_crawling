SHOW DATABASES;

CREATE DATABASE testdb;
USE testdb;

SHOW TABLES;

CREATE TABLE codes(
	fullCd CHAR(07) PRIMARY KEY,
	korNm VARCHAR(20) NOT NULL,
	engNm VARCHAR(20)
)

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

/*자료 삭제 */
DELETE FROM codes;

/*자료 확인 */
SELECT * FROM codes;

/*자료 수정 */
UPDATE codes
SET korNm = REPLACE(kornm, "시","광역시");

UPDATE codes
SET korNm = "서울특별시"
WHERE fullcd = "0105001"

UPDATE codes SET korNm = "세종시" WHERE fullcd="0105017"

#select 구문을 잘 사용해서 원하는 자료를 뽑아낸다.
SELECT * FROM codes WHERE korNm LIKE "%광역시";
SELECT korNm FROM codes WHERE korNm LIKE "%광역시"
ORDER BY korNm DESC;

SELECT SUBSTRING(fullcd,6,1) AS c3 ,
	SUBSTRING(fullcd,7,1) AS c4
FROM codes;

SELECT SUBSTRING(fullcd,6,1) AS c3 ,
	COUNT(*) AS cnt
FROM codes
GROUP BY c3
HAVING cnt >= 9	#그룹화 하면 where말고 having
;
