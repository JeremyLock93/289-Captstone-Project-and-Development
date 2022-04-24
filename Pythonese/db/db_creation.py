import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'tempholics'

TABLES = {}
TABLES['templates'] = (
" IF NOT EXISTS CREATE TABLE TEMPLATES ("
" TID NUMBER(10)," 
" Class_name VARCHAR2(25)," 
" Creation_date DATE DEFAULT SYSDATE," 
" CONSTRAINT templates_tid_pk PRIMARY KEY(TID))"
)

TABLES['template_data'] = (
" IF NOT EXISTS CREATE TABLE TEMPLATE_DATA("
" AID NUMBER(10),"
" TID NUMBER(10),"
" Assignment_name VARCHAR2(25)," 
" Due_date DATE,"
" Comments VARCHAR2(150),"
" CONSTRAINT template_data_aid_pk PRIMARY KEY(AID), "
" CONSTRAINT template_data_tid_fk FOREIGN KEY(TID)"
    "REFERENCES TEMPLATES(TID))"
)

TABLES['files'] = (
" IF NOT EXISTS CREATE TABLE FILES("
" FID NUMBER(10)," 
" File_name VARCHAR2(30),"
" File_type VARCHAR2(10),"
" File_size VARCHAR2(10)," 
" Upload_date DATE DEFAULT SYSDATE," 
 " CONSTRAINT templates_fid_pk PRIMARY KEY(FID))"
)

TABLES['users'] = (
"IF NOT EXISTS CREATE TABLE USERS("
" USID NUMBER(5),"
" Username VARCHAR2(15) NOT NULL,"
" LastName VARCHAR2(20) NOT NULL,"
" FirstName VARCHAR2(15) NOT NULL,"
" Email VARCHAR2(30), "
" Password VARCHAR2(25), "
" Affiliation CHAR(2), "
" Join_date DATE DEFAULT SYSDATE, "
" TID NUMBER(10), "
" FID NUMBER(10), "
" CONSTRAINT users_USID_pk PRIMARY KEY (USID), "
" CONSTRAINT users_TID_fk FOREIGN KEY (TID)"
    " REFERENCES TEMPLATES(TID),"
  "CONSTRAINT users_FID_fk FOREIGN KEY (FID)"
    "REFERENCES FILES(FID))"
)

cnx = mysql.connector.connect(user= 'root')
cursor = cnx.cursor()

def create_database(cursor):
  try:
    cursor.execute(
      "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf-8'".format(DB_NAME))
  except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))
    exit(1)
    

  try:
    cursor.execute("USE {}".format(DB_NAME))
  except mysql.connector.Error as err:
    print("Database {} does not exists".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
      create_database(cursor)
      print("Database {} created sucessfully.".format(DB_NAME))
      cnx.database = DB_NAME
    else:
      print(err)
      exit(1)
      

for table_name in TABLES:
  table_description = TABLES[table_name]
  try:
    print("Creating table {}: ".format(table_name), end = '')
    cursor.execute(table_description)
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
      print("already exists")
    else:
      print(err.msg)
  else:
    print("Ok")
    
cursor.close()
cnx.close()