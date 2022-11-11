-- create a table
CREATE TABLE CUSTOMERS(
  ID   INT              NOT NULL,
  NAME VARCHAR (20)     NOT NULL,
  AGE  INT              NOT NULL,
  ADDRESS  CHAR (25) ,
  SALARY   DECIMAL (18, 2),       
  PRIMARY KEY (ID)
);
-- insert some values
INSERT INTO CUSTOMERS VALUES (1, 'Ryan', 22, '22222', 10000);
INSERT INTO CUSTOMERS VALUES (2, 'Joanna', 34, '22222', 10000);
-- fetch some values
SELECT * FROM CUSTOMERS;