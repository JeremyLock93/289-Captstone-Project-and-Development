/*
  Taylor J. Brown
  28FEB22
  This is the database initialization file for the website.
  ---
    It will drop and cascade all tables and their constrants if they exist
    then it will create all of the required columns and data types along with the 
    data types to be stored with.
  ---
*/


DROP TABLE IF EXISTS TEMPLATES CASCADE CONSTRAINTS;
DROP TABLE IF EXISTS TEMPLATE_DATA CASCADE CONSTRAINTS;
DROP TABLE IF EXISTS FILES CASCADE CONSTRAINTS;
DROP TABLE IF EXISTS USERS CASCADE CONSTRAINTS;


CREATE TABLE TEMPLATES (
TID NUMBER(10), 
Class_name VARCHAR2(25), 
Creation_date DATE DEFAULT SYSDATE, 
  CONSTRAINT templates_tid_pk PRIMARY KEY(TID));


CREATE TABLE TEMPLATE_DATA(
AID NUMBER(10),
TID NUMBER(10), 
Assignment_name VARCHAR2(25), 
Due_date DATE,
Comments VARCHAR2(150), 
  CONSTRAINT template_data_aid_pk PRIMARY KEY(AID),
  CONSTRAINT template_data_tid_fk FOREIGN KEY(TID)
    REFERENCES TEMPLATES(TID));


CREATE TABLE FILES(
FID NUMBER(10), 
File_name VARCHAR2(30),
File_type VARCHAR2(10),
File_size VARCHAR2(10), 
Upload_date DATE DEFAULT SYSDATE, 
  CONSTRAINT templates_fid_pk PRIMARY KEY(FID));


CREATE TABLE USERS(
USID NUMBER(5),
Username VARCHAR2(15) NOT NULL,
LastName VARCHAR2(20) NOT NULL,
FirstName VARCHAR2(15) NOT NULL,
Email VARCHAR2(30),
Password VARCHAR2(25),
Affiliation CHAR(2),
Join_date DATE DEFAULT SYSDATE,
TID NUMBER(10),
FID NUMBER(10),
  CONSTRAINT users_USID_pk PRIMARY KEY (USID),
  CONSTRAINT users_TID_fk FOREIGN KEY (TID)
    REFERENCES TEMPLATES(TID),
  CONSTRAINT users_FID_fk FOREIGN KEY (FID)
    REFERENCES FILES(FID));


COMMIT;
