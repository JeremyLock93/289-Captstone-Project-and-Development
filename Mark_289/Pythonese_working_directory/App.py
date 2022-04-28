import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file

app = Flask(__name__)
USER_DATA = os.path.join('static','user_data')

app.config['user_info'] = USER_DATA

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
    PROFILE_PIC = os.path.join(app.config['user_info'], 'profile_pic.jpg')
    USERNAME = os.path.join(app.config['user_info'], 'user_info.json')
    NAME = os.path.join(app.config['user_info'], 'user_info.json')
    EMAIL = os.path.join(app.config['user_info'], 'user_info.json')
    PASSWORD = os.path.join(app.config['user_info'], 'user_info.json')
    return render_template("profile.html",
        profile_pic = PROFILE_PIC,
        username = USERNAME,
        name = NAME,
        email = EMAIL,
        password = PASSWORD)
    



@app.route("/loggin")
def loggin():
    return render_template("loggin.html")


@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")



if __name__ == "__main__":
	app.run(debug=True)