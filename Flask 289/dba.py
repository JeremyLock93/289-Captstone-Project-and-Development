""" from getpass import getpass
from mysql.connector import connect, Error

#The creation of the connection for the database. 
templaholicDB = mysql.connector.connect(
    host = "",
    user = "",
    passwd = "",
    database = ""
)

#The cursor Instance to interact with the database
cursor = templaholicDB.cursor()

#Creating the Database 
#templaholicDB.cursosr.execute() """