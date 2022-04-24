import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc

app = Flask(__name__)



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


@app.route("/profile", methods = ['GET', 'POST'])
def profile():
        return render_template("profile.html")
      

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
    
        


@app.route("/sign-up", methods = ['GET', 'POST'])
class RegistrationForm(form):
    username = TextField('UserName',[validators.Length(min=5, max = 15)])
    lastname = TextField('LastName', [validators.Length(min=5, max=20)])
    firstname = TextField('FirstName', [Validators.Length(min=5, max=15)])
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
        


if __name__ == "__main__":
	app.run(debug=True)