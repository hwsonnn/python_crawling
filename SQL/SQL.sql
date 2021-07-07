SHOW DATABASES ;

CREATE DATABASE mydb ;	#my db라는 데이터베이스 실행

USE mydb ;

SHOW tables ;

CREATE TABLE codes (

	fullcd CHAR(07) PRIMARY KEY,

	kornm VARCHAR(20) NOT NULL,

	engnm VARCHAR(20)

	)

SHOW tables ;	# codes라는 table 생성된 것 확인 가능

DESC codes ; 

 

SELECT * FROM codes ;

INSERT INTO codes (fullcd, kornm, engnm)

VALUES ('0105001', 'Seoul', '') ;





SHOW DATABASES ;

USE mydb2 ;

SHOW TABLES ;

DESC codes ;

SHOW VARIABLES LIKE 'c%' ;

DROP TABLE codes ;

CREATE TABLE codes (

	fullcd CHAR(07) PRIMARY KEY,

	kornm VARCHAR(20) NOT NULL,

	engnm VARCHAR(20)

)

 

SELECT * FROM codes ;

 

INSERT INTO codes (fullcd, kornm, engnm)

VALUES ('0105001', '서울시', '') ;
