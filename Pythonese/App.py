from email import message
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
        # Scrapes the loggin form text boxes
        email = request.form['email']
        email = email.lower()
        password = request.form['password'] # Case sensitive!!!
        
        # TODO Validate if the user has selected remember me. If "yes" set cookie to expire never if "no" set cookie to expire at midnight

        # Gets the stored hashed password from the DB based on the email entered 
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT Password FROM users WHERE Email LIKE '{0}' '''.format(email))
        user = cursor.fetchall()
        cursor.close()
        
        # Catches a null value return if email doesn't exist in DB
        try:
            dbpass = user[0][0]
        except IndexError:
            title = 'Invalid credentials'
            message = 'You may have entered in the wrong email or password for your account'
            modal = popUp(title, message)
            return render_template('loggin.html', modal = modal)

        # Compairs the entered password with the stored hash version of the password 
        # if error occurs it will present the user with a pop up and a re-try event
        if bcrypt.checkpw(password.encode('utf-8'), dbpass.encode('utf-8')):
            return render_template('index.html')
        else:
            title = 'Invalid credentials'
            message = 'You may have entered in the wrong email or password for your account'
            modal = popUp(title, message)
            return render_template('loggin.html', modal = modal)


@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")


@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return "Sign up via the sign upForm"

    if request.method == 'POST':
        # Scrapes the sign up form text boxes
        username = request.form['username']

        lastname = request.form['lastname']

        firstname = request.form['firstname']

        email = request.form['email'] # The email is stored in the DB in all lowercase letters, because it allows us to add their emails to a mailing list later on.
        email = email.lower()

        password = request.form['password']
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) # Default passes is 12 prefix is 2b

        affiliation = request.form['affiliation'] # Alters the affiliation to be a single char for DB insert
        if affiliation == "Student":
            affiliation = 'S'
        else:
            affiliation = 'T'

        # Adds the user into the DB with their entered fields 
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users VALUES(null,%s,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP)''',(username,lastname,firstname,email,hashed,affiliation))
        mysql.connection.commit()
        cursor.close()

        # TODO Create session cookie with users information 

        # Redirects the user to the home page 
        return render_template("index.html")


"""
    You can use this method to create a pop up message for anything by passing 
    a title and a message to this method it will then return the HTML and JS 
    as a docstring using Markup.
"""
def popUp(title, message):
    return Markup("""
                    <div class="popup active" id="popup-1">
                        <div class="overlay"></div>
                        <div class="content">
                            <div class="close-btn" onclick="togglePopup()">&times;</div>
                            <h1>""" + title + """</h1>
                            <p>""" + message + """</p>
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
 