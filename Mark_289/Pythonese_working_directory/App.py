import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file

app = Flask(__name__)
USER_FOLDER = os.path.join("static","user_data")

app.config["User_Folder"] = USER_FOLDER

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
    PROFILE_PIC = "NONE" #os.path.join(app.config['user_data'], 'profile_pic.jpg')
    USERNAME = "NONE" #os.path.join(app.config['user_data'], 'user_info.json')
    NAME = "NONE" #os.path.join(app.config['user_data'], 'user_info.json')
    EMAIL = "NONE" #os.path.join(app.config['user_data'], 'user_info.json')
    PASSWORD = "NONE" #os.path.join(app.config['user_data'], 'user_info.json')
    return render_template("profile.html",
        PROFILE_PIC = PROFILE_PIC,
        USERNAME = USERNAME,
        NAME = NAME,
        EMAIL = EMAIL,
        PASSWORD = PASSWORD)
    



@app.route("/loggin")
def loggin():
    return render_template("loggin.html")


@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")



if __name__ == "__main__":
	app.run(debug=True)