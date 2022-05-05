import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file
from flask_mysqldb import MySQL
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
import gc

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'Pythonese.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'Pythonese'
app.config['MYSQL_PASSWORD'] = 'password-123'
app.config['MYSQL_DB'] = 'Pythonese$Templiholic_DB'

mysql = MySQL(app)


@app.route("/home", methods = ['GET', 'POST'])
@app.route("/", methods = ['GET', 'POST'])
def index():
	return render_template("index.html")


@app.route("/calendar", methods = ['GET', 'POST'])
def calendar():
    return render_template("calendar.html")


@app.route("/templates", methods = ['GET', 'POST'])
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

@app.route("/loggin", methods = ['GET', 'POST'])
def loggin():
    return render_template("loggin.html")      


#WE NEED TO RE_WORK THE LOGGIN
"""
@app.route("/loggin", methods = ['GET', 'POST'])
def loggin():
    error = ''
    try:
        cnx, conn = connecetion()
        if request == 'POST':
            data = cnx.execute("SELECT * FROM users WHERE username = (%s)",
                           thwart(request.form['username']))
            data = cnx.fetchone()[2]
            
            if sha256_crypt.verify(request.form['password'], data):
                session['logged_in'] = True
                session['username'] = request.form['username']
            
            flash("You are now Logged In")
            return redirect(url_for("home"))
        
        else:
            error = "Invalid credentials Please Try again"
        gc.collect()  
            
        return render_template("loggin.html")
    
    except Exception as e:
        error = "Invalid credentials Please Try again"
"""


@app.route("/sign-up", methods = ['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html")    


#WE NEED TO FINISH UP THE USER CREATION DATA VALIDATION        
@app.route('/signup', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        username = request.form['username']
        lastname = request.form['lastname']
        firstname = request.form['firstname']
        email = request.form['email']
        email = email.lower()
        password = request.form['password']
        affiliation = request.form['affiliation']
        if affiliation == "Student":
            affiliation = 'S'
        else:
            affiliation = 'T'

        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users VALUES(null,%s,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP)''',(username,lastname,firstname,email,password,affiliation))
        mysql.connection.commit()
        cursor.close()
        return render_template("index.html")
    
    
    
"""
@app.route("/sign-up", methods = ['GET', 'POST'])
class RegistrationForm(form):
    username = TextField('UserName',[validators.Length(min=5, max = 15)])
    lastname = TextField('LastName', [validators.Length(min=5, max=20)])
    firstname = TextField('FirstName', [validators.Length(min=5, max=15)])
    email = TextField('Email', [validators.Length(min=6, max=30)])
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
        ])
    confirm = PasswordField('Repeat Password')
    affliation = TextField('Affliation', [validators.required])
    accept_tos = BooleanField('I accept the Terms of Service', [validators.Required()])
    
    def sign_up():
        try:
            form = RegistrationForm(request.form)
            
            if request.method == 'POST' and form.validate():
                username = form.username.data
                lasname = form.lastname.data
                firstname = form.firstname.data
                email = form.email.data
                password = shaw256.encrypt((str(form.password.data)))
                affliation = form.affliation.data
                cnx, conn = mysql.connector.connect(user= 'root')
                
                x = cnx.execute("SELECT * FROM user WHERE username = (%s)",
                                (thwart(username)))
                
                if int(x) > 0:
                    flash("That username is already taken, please choose another")
                    return render_template("sign_up.html", form=form)
                else: 
                    cnx.execute("INSERT INTO users (username, lastname, firstname, email, password, affliation) VALUES (%s, %s, %s, %s, %s, %s)",
                                (thwart(username), thwart(lastname), thwart(firstname), thwart(email), thwart(password), thwart(affiliation)))
                    
                    cnx.commit()
                    flash("Thank you for registering")
                    cnx.close()
                    conn.close()
                    gc.collect()
                    
                    session['logged_in'] = True
                    session['username'] = username
                    
                    return redirect(url_for('/home'))
                
                return render_template("sign_up.html")
            
        except Exception as e:
            return(str(e))
"""        
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
