show databases;
create database School;
CREATE TABLE USERS(
ID integer auto_increment primary key,
    NAME varchar(100),
    AGE integer,
    GRADE varchar(10)
    );	
 SELECT * from USERS;   
 INSERT into USERS(NAME,AGE,GRADE) values('naveen',23,'A'),('janu',25,'C'),('sumithra',45,'B');
 SELECT * from USERS; 
 
   