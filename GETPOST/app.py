try:
    from io import BytesIO

    from flask import (Flask, redirect, render_template, request, send_file,
                       url_for)
    from flask_wtf import Form
    from flask_wtf.file import FileField
    from wtforms import SubmitField
    print("All Modules Loaded .... ")
except:
    print (" Some Module are missing ...... ")

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='database',
                                         user='user',
                                         password='password', use_pure=True)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


@app.route('/', methods=["GET", "POST"])
def index():

    form = UploadForm()
    if request.method == "POST":

        if form.validate_on_submit():
            file_name = form.file.data
            database(name=file_name.filename, data=file_name.read() )
            return render_template("home.html", form=form)

    return render_template("home.html", form=form)


@app.route('/download', methods=["GET", "POST"])
def download():

    form = UploadForm()

    if request.method == "POST":

        conn= sqlite3.connect("YTD.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  my_table """)

        for x in c.fetchall():
            name_v=x[0]
            data_v=x[1]
            break

        conn.commit()
        cursor.close()
        conn.close()

        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)


    return render_template("home.html", form=form)




class UploadForm(Form):
    file = FileField()
    submit = SubmitField("submit")
    download = SubmitField("download")

def database(name, data):
    conn= sqlite3.connect("YTD.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS my_table (name TEXT,data BLOP) """)
    cursor.execute("""INSERT INTO my_table (name, data) VALUES (?,?) """,(name,data))

    conn.commit()
    cursor.close()
    conn.close()



def query():
        conn= sqlite3.connect("YTD.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  my_table """)

        for x in c.fetchall():
            name_v=x[0]
            data_v=x[1]
            break

        conn.commit()
        cursor.close()
        conn.close()

        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
