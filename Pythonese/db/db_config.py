import MySQLdb

def connection():
    cnx = MySQLdb.connect(user = 'root', 
                              password = '',
                              host = 'localhost', 
                              database = 'Templholic_DB')

    c = cnx.cursor()