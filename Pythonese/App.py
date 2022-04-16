import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file

app = Flask(__name__)



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
    return render_template("profile.html")


@app.route("/loggin")
def loggin():
    return render_template("loggin.html")


@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")



if __name__ == "__main__":
	app.run(debug=True)