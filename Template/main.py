import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file



app = Flask(__name__)

@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + "<b><a herf = '/logout'>click here to log out</a></b>"
    return "YOu are not logged in <br><a herf = '/login'>" + "click here to login in</a<"

@app.rout('/login', methods =["POST", "GET"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''<form action = ""method = "post">
                <p>input type = text name = username/></p>
                <p input type = submit value = Login/></p>
            </form>
            '''
            
@app.route('/logout')
def logout():
    #Removes username sessions if there is a session if there is one
    sesssion.pop('username', None)
    return redirect(url_for('index'))

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/setcookie', method = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        
        resp = mae_response(render_template('setcookie.html'))
        resp = set_cookie('userID', user)
        
        return resp
    
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1> Welcome' + name +'</h1>'



if __name__ == "__main__":
    app.run(debug = True)