import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file
from flask_mysqldb import MySQL
import bcrypt
from markupsafe import Markup

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'templiholics_db'

mysql = MySQL(app)

@app.route("/home")
@app.route("/")
def index():
	return render_template("index.html")


@app.route("/calendar")
def calendar():
    return render_template("calendar.html")


@app.route("/templates")
def templates():
    return render_template("templates.html")


@app.route("/profile")
def profile():
    userRecord = Test()

    return render_template("profile.html",
        username = userRecord[1],
        name = userRecord[3] +" "+ userRecord[2],
        email = userRecord[4],
        password = userRecord[5])


@app.route("/loggin")
def loggin():
    return render_template("loggin.html")


@app.route("/log", methods = ['POST', 'GET'])
def log():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        email = request.form['email']
        email = email.lower()
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT Password FROM users WHERE Email LIKE '{0}' '''.format(email))
        user = cursor.fetchall()
        cursor.close()
        
        dbpass = user[0][0]

        if bcrypt.checkpw(password.encode('utf-8'), dbpass.encode('utf-8')):
            return render_template('index.html')
        else:
            popUp = invalidLog()
            return render_template('loggin.html', popUp = popUp)


@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")


@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return "Sign up via the sign upForm"

    if request.method == 'POST':
        username = request.form['username']

        lastname = request.form['lastname']

        firstname = request.form['firstname']

        email = request.form['email']
        email = email.lower()

        password = request.form['password']
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        affiliation = request.form['affiliation']
        if affiliation == "Student":
            affiliation = 'S'
        else:
            affiliation = 'T'

        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users VALUES(null,%s,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP)''',(username,lastname,firstname,email,hashed,affiliation))
        mysql.connection.commit()
        cursor.close()

        return render_template("index.html")



def invalidLog():
    return Markup("""
                    <div class="popup active" id="popup-1">
                        <div class="overlay"></div>
                        <div class="content">
                            <div class="close-btn" onclick="togglePopup()">&times;</div>
                            <h1>Invalid credentials</h1>
                            <p>You may have entered in the wrong email or password for your account</p>
                        </div>
                    </div>
                    <script>
                        function togglePopup(){
                            document.getElementById("popup-1").classList.toggle("active");
                        }
                    </script>
                """)


def Test():
    USID = 1
    UserName = 'Admin'
    lastname = 'Templiholics'
    firstname = 'Pythonese'
    email = 'admin@Pythonese.com'
    password = 'We_Are_A_Team$50'
    affiliation = 'A'
    datecreated = '2022-04-28 02:59:24'
    return(USID,UserName,lastname,firstname,email,password,affiliation,datecreated)







if __name__ == "__main__":
	app.run(debug=True)
 