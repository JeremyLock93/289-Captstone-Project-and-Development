import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file

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
        return render_template("loggin.html")
        if request.method == 'POST':
            session['username'] = request.form ['username']
            return redirect(url_for('home'))
        return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''   
        


@app.route("/sign-up", methods = ['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html")
    


if __name__ == "__main__":
	app.run(debug=True)