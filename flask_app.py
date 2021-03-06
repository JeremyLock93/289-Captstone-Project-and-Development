import os
from xml.etree.ElementTree import Comment
import bcrypt
import re
import File_Parse_onefile as fp
from flask import Flask, redirect, url_for, render_template, request, session
from flask_wtf import FlaskForm
from flask_mysqldb import MySQL
from markupsafe import Markup
from dotenv import load_dotenv
from datetime import timedelta
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired


"""
    If you have missing modules run 
    
    Windows:
    pip install -r requirements.txt
    
    Mac:
    python -m pip install requirements.txt
"""


# The uploaded .env is for a local enviroment 
# for security purposes the .env on the running site has been left out of this repo
load_dotenv()

app = Flask(__name__)

app.config["FILE_UPLOADS"] = "static/files"
app.config["ALLOWED_FILE_EXTENSIONS"] = ["DOCX","CSV"]

app.secret_key = os.getenv("SECRET_KEY")

app.permanent_session_lifetime = timedelta(days=7)

app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

mysql = MySQL(app)

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route("/home")
@app.route("/")
def index():
    if "username" in session:
        """
            queries the usertemplates to get the TID
            queries the template to get the classnames
            queries the templatedata to get all assignments associated with the user
            sends data to html
        """
        USID = session['USID']
        
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT TID FROM usertemplates WHERE USID = '{0}' '''.format(USID))
        templateTIDs = cursor.fetchall()
        cursor.close()
        
        classNames = []
        
        cursor = mysql.connection.cursor()
        for record in templateTIDs:
            TID = record[0]
            cursor.execute(''' SELECT ClassName FROM templates WHERE TID = '{0}' '''.format(TID))
            classNames += cursor.fetchall()
        cursor.close()
        
        table = ""
        
        cursor = mysql.connection.cursor()
        
        count = 0
        for record in templateTIDs:
            
            TID = record[0]
            cursor.execute(''' SELECT AssignmentName, DueDate, Comments FROM templatedata WHERE TID = '{0}' '''.format(TID))
            assignments = cursor.fetchall()
            
            name = classNames[count][0]
            count += 1
            tablehead = ""
            tablehead += Markup("""
                                <table class="table table-dark table-striped">
                                    <thead>
                                    <table class="table table-dark table-striped" style="margin-bottom: 5%;">
                                        <thead>
                                        <tr><th colspan="3"><h1 style="font-weight: bold; font-size: 34px;">""" + name + """</h1></th></tr>
                                        <tr>
                                            <th scope="col" style="text-align:center;">Assignment Name</th>
                                            <th scope="col" style="text-align:center;">Due Date</th>
                                            <th scope="col" style="text-align:center;">Comments</th>
                                        </tr>
                                    </thead>
                                    <tbody>""")
            

            tablebody = ""
            for data in assignments:
                nameA = data[0]
                date = data[1]
                Comment = data[2]
                tablebody += Markup(""" <tr>
                                            <td>""" + nameA + """</td>
                                            <td>""" + date + """</td>
                                            <td>""" + Comment + """</td>
                                        </tr>
                                    """)

            
                                    
            table += tablehead + tablebody +  Markup("""     </tbody>
                                                        </table> 
                                                    """)
            del assignments                           
        cursor.close()
        
        if table == "":
            nothing = Markup("""
                                <div class="default-home">
                                    <div style="float:left; padding-top:15%; padding-left: 10%;">
                                        <H1 style="padding-bottom: .25em; font-size: 64px; font-weight: bold;">Oh No!</H1>
                                        <P style="padding-bottom: 1.5em;">It would seem like you havent uploaded a template yet</P>
                                        <a href="templates"><button type="button" class="btn btn-primary">Click Here to add a template</button></a>
                                    </div>
                                        <img src="static/stockimage/Robot.png" default="Robot" style="max-width: 600px; max-height:600px; float: right;">
                                </div>
                             """)
            return render_template("index.html",
                                   default=nothing)
        else:
            return render_template("index.html", 
                               table=table)
    else:
        return redirect(url_for("loggin"))
	


@app.route("/calendar")
def calendar():
    if "username" in session:
        return render_template("calendar.html")
    else:
        return redirect(url_for("loggin"))
    


@app.route("/templates", methods=['GET','POST'])
def templates():
    if "username" in session:
        if request.method == "POST":
            
            if request.files:
                    file = request.files["file"]

                    if file.filename == "":
                        title = 'Our apologies for the inconvenience'
                        message = "<li>It seems like you haven't choosen a file to upload yet!</li>"
                        modal = popUp(title, message)
                        return render_template('templates.html', 
                                                modal = modal)

                    if allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        className = request.form['className']
                        
                        USID = str(session['USID'])
                        
                        new_fileName = USID + '-' + session['username'] + '-' + filename
                        
                        file.save(os.path.join(app.config["FILE_UPLOADS"], new_fileName))
                        
                        pass_fail = record_creation(new_fileName,className)
                        
                        if pass_fail == True:
                            title = 'Success!'
                            message = "<li>Your file has been uploaded successfuly!</li>"
                            modal = popUp(title, message)
                            return render_template('templates.html', 
                                                    modal = modal)
                        else:
                            title = 'Oh No!'
                            message = "<li>We were unable to process your file!</li>"
                            modal = popUp(title, message)
                            return render_template('templates.html', 
                                                    modal = modal)
                    else:
                        title = 'Our apologies for the inconvenience'
                        message = "<li>Unfortuantly we dont support that file type.</li>"
                        modal = popUp(title, message)
                        return render_template('templates.html', 
                                                modal = modal)

        return render_template("templates.html")
    
    else:
        return redirect(url_for("loggin"))
    
    
@app.route("/profile")
def profile():
    if "username" in session:
        return render_template("profile.html",
        username = session["username"],
        name = session["first"] +" "+ session["last"],
        email = session["email"])
    else:
        return redirect(url_for("loggin"))
    

@app.route("/change", methods = ['POST', 'GET'])
def change():
    if "username" in session:
        if request.method == 'POST':
            currentPass = request.form['currentPass']
            newPass = request.form['password']
            hashed = bcrypt.hashpw(newPass.encode('utf-8'), bcrypt.gensalt()) # Default passes is 12 prefix is 2b
            email = session["email"]
            
            # Validates the passwords requirements
            result = passStandardCheck(newPass)
            
            if result == False:
                title = 'Our apologies for the inconvenience'
                message = "<li>Your password must contain an uppercase letter a lowercase letter and a symbol</li>"
                modal = popUp(title, message)
                return render_template('changepass.html', 
                                        modal = modal,
                                        username = session["username"])
            
# Gets the stored hashed password from the DB based on the email entered 
            cursor = mysql.connection.cursor()
            cursor.execute(''' SELECT Password FROM users WHERE Email LIKE '{0}' '''.format(email))
            user = cursor.fetchall()
            cursor.close()
            dbpass = user[0][0]
            
            if bcrypt.checkpw(currentPass.encode('utf-8'), dbpass.encode('utf-8')):
                cursor = mysql.connection.cursor()
                cursor.execute(''' UPDATE users SET Password = %s WHERE email = %s ''',[hashed, email])
                mysql.connection.commit()
                cursor.close()
                
                return redirect(url_for("profile"))
            else:
                title = 'Invalid credentials'
                message = '<li>You may have entered in the wrong password for your account.</li>'
                modal = popUp(title, message)
                return render_template('changepass.html', 
                                        modal = modal,
                                        username = session["username"])
        else:
            return render_template("changepass.html",username = session["username"])
    else:
        return redirect(url_for("loggin")) 


@app.route("/loggin", methods = ['POST', 'GET'])
def loggin():
    if request.method == 'POST':
# Scrapes the loggin form text boxes
        email = request.form['email']
        email = email.lower()
        password = request.form['password'] # Case sensitive!!!
        remember = request.form.get('remember')

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
            message = '<li>You may have entered in the wrong email or password for your account.</li>'
            modal = popUp(title, message)
            return render_template('loggin.html', modal = modal)

# Compairs the entered password with the stored hash version of the password 
# if error occurs it will present the user with a pop up and a re-try event
        if bcrypt.checkpw(password.encode('utf-8'), dbpass.encode('utf-8')):
            if remember == 'on':
                CreatePermSession(email)
            else:
                CreateSession(email) # Server side session creation
            
            return redirect(url_for("index"))
        else:
            title = 'Invalid credentials'
            message = '<li>You may have entered in the wrong email or password for your account.</li>'
            modal = popUp(title, message)
            return render_template('loggin.html', modal = modal)

# If no POST method was called the log in page is rendered
    else:
        return render_template("loggin.html")
        


@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
# Initalized incase modal is needed
        modal = False
        title = 'Our apologies for the inconvenience'
        message = ''
        
# Scrapes data from sign up form
        username = request.form['username']
        lastname = request.form['lastname']
        firstname = request.form['firstname']
        email = request.form['email'] # The email is stored in the DB in all lowercase letters, because it allows us to add their emails to a mailing list later on.
        email = email.lower()
        password = request.form['password']
        affiliation = request.form['affiliation'] 
        
# Validates the passwords requirements then hashes and salts the password
        result = passStandardCheck(password)
        
        if result == False:
            message += "<li>Your password must contain an uppercase letter a lowercase letter and a symbol</li><br>"
            modal = True

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) # Default passes is 12 prefix is 2b
        
# Alters the affiliation to be a single char for DB insert
        if affiliation == "Student":
            affiliation = 'S'
        else:
            affiliation = 'T'

# Query to check if user the username and/or email is in the DB already
# & Modal creation if data exists
        usrExists = False

        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM users WHERE username = %s ''',[username])
        UsernameCheck = cursor.fetchall()
        cursor.close()
        
        try:
            UsernameCheck = UsernameCheck[0][0]
            message += '<li>Unfortunately that username is not available.</li><br>'
            usrExists = True
        except:
            pass
        
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM users WHERE email = %s ''',[email])
        EmailCheck = cursor.fetchall()
        cursor.close()
        
        try:
            EmailCheck = EmailCheck[0][0]
            message += '<li>There seems to be an account with that email with us already.</li><br>'
            usrExists = True
        except:
            pass 
            
        if usrExists == True or modal == True:
            modal = popUp(title, message)
            return render_template('sign_up.html', modal = modal)

# Adds the user into the DB with their entered fields 
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users VALUES(null,%s,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP)''',[username,lastname,firstname,email,hashed,affiliation])
        mysql.connection.commit()
        cursor.close()

# Server side session
        CreateSession(email)   

        # Redirects the user to the home page 
        return redirect(url_for("index")) 
    
# If no POST method was called the sign up page is rendered
    else:
        return render_template("sign_up.html")
    
    
@app.route("/logout")
def logout():
    """
        This method deletes the users client session cookie from their browser
    """
    if "username" in session:
        session.pop("USID", None)
        session.pop("username", None)
        session.pop("last", None)
        session.pop("first", None)
        session.pop("email", None)
        return redirect(url_for("loggin"))
    else:
        return redirect(url_for("loggin"))


def popUp(title, message):
    """
        You can use this method to create a pop up message for anything by passing 
        a title and a message to this method it will then return the HTML and JS 
        as a docstring using Markup.
    """
    return Markup("""
                    <div class="popup active" id="popup-1">
                        <div class="overlay"></div>
                        <div class="content">
                            <div class="close-btn" onclick="history.back()">&times;</div>
                            <h1 style="font-weight: bold;">""" + title + """</h1>
                            <ul>""" + message + """</ul>
                        </div>
                    </div>
                """)
    
    
def CreateSession(email):
    """
        This method queries the DB then it creates 
        a session cookie on the sever.
        
        This only lasts until the user closes their browser or logs out
    """
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM users WHERE email = %s ''',[email])
    user = cursor.fetchall()
    cursor.close()
    
    session["USID"] = user[0][0]
    session["username"] = user[0][1]
    session["last"] = user[0][2]
    session["first"] = user[0][3]
    session["email"] = user[0][4]
    
    
def CreatePermSession(email):
    """
        This method queries the DB then it creates 
        a session cookie on the clients browser.
        
        This lasts for 14 days then it will delete it's self 
        or until the user logs out
    """
    session.permanent = True
    
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM users WHERE email = %s ''',[email])
    user = cursor.fetchall()
    cursor.close()
    
    session["USID"] = user[0][0]
    session["username"] = user[0][1]
    session["last"] = user[0][2]
    session["first"] = user[0][3]
    session["email"] = user[0][4]


def passStandardCheck(password):
    """
        This method checks the passed variable to see if it is greater 
        than 6 characters long has an uppercase letter a 
        lowercase letter and a symbol.
    """
    result = False
    if len(password) < 6:
        result = False 
    
    for char in password:
        if char.isupper():
            result = True
            break
        else:
            result = False
        
    for char in password:
        if char.islower():
            result = True
            break
        else:
            result = False
        
    regex = re.compile('[-@_!#$%^&*()<>?/\|}{~:]')
    
    if(regex.search(password) != None):
        result = True
    else:
        result = False
        
    return result


def allowed_file_filesize(filesize):

    if int(filesize) <= app.config["MAX_FILE_FILESIZE"]:
        return True
    else:
        return False
    
    
def allowed_file(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False


def record_creation(filename,Classname):
    ext = filename.rsplit(".", 1)[1]
    File_location = 'C:\\Users\\Taylor\\Documents\School\\4_Spring_2022\\CSC-289 Programming Capstone Project\\Pythonese\\static\\files' + '\\' + filename

    if ext.upper() == "CSV":
        DATA = fp.ParseCSV(File_location)


    if ext.upper() == "DOCX":
        DATA = fp.ParseDOCX(File_location)

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO templates VALUES(null,%s,CURRENT_TIMESTAMP,%s)''',[Classname, File_location])
        mysql.connection.commit()
        cursor.close()
        
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM templates WHERE ClassName = %s ''',[Classname])
        data = cursor.fetchall()
        cursor.close()
        TID = data[0][0]
        USID = session['USID'] 
        
        cursor = mysql.connection.cursor()
        mySql_insert_query = """INSERT INTO usertemplates (Record,USID,TID) VALUES (null,%s, %s) """
        record = (USID,TID)
        cursor.execute(mySql_insert_query, record)
        mysql.connection.commit()
        
        for record in DATA:
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO templatedata VALUES(null,%s,%s,%s,%s)''',[TID, record['Assignment'], record['Due-Date'], record['Comment']])
            mysql.connection.commit()
            cursor.close()
            
        return True
    
    except:
        return False


if __name__ == "__main__":
	app.run(debug=True)
 