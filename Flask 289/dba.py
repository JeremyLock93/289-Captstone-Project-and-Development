from getpass import getpass
from mysql.connector import connect, Error



def get_db_connection():
    try:
        with connect(
            host = "local host";
            user = input("Enter username: "),
            password=getpass("Enter password: "),
        ) as connection:
            create_db_query = ""
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
            print(connection)
    except Error as e:
        print(e)
