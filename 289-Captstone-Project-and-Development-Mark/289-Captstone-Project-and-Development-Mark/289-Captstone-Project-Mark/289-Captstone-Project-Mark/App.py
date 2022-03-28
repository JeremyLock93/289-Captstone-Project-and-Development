import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")
@app.route("/homepage")
def homepage():
	return render_template("main.html")


if __name__ == "__main__":
	app.run()