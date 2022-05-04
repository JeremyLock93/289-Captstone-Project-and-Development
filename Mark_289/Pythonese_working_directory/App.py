import sys
import io
import os
from flask import Flask, flash, redirect, url_for, render_template, request, send_file
from werkzeug.utils import secure_filename
from Test import Test


UPLOAD_FOLDER = 'static/user_info'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
USER_DATA = os.path.join('static','user_data')


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/profile")
def profile():
    
    PROFILE_PIC = os.path.join(app.config['user_info'], 'profile_pic.jpg')
    '''USERNAME = os.path.join(app.config['user_info'], 'user_info.json')
    NAME = os.path.join(app.config['user_info'], 'user_info.json')
    EMAIL = os.path.join(app.config['user_info'], 'user_info.json')
    PASSWORD = os.path.join(app.config['user_info'], 'user_info.json')'''
    userRecord = Test()


    return render_template("profile.html",
        profile_pic = PROFILE_PIC,
        username = userRecord[1],
        name = userRecord[3] +" "+ userRecord[2],
        email = userRecord[4],
        password = userRecord[5])



'''
@app.route("/upload-image", methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''



@app.route("/loggin")
def loggin():
    return render_template("loggin.html")


@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")



if __name__ == "__main__":
	app.run(debug=True)