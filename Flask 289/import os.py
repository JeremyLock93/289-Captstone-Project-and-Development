""" import os
from flask import Flask

def create_app(test_config=None):
    #Creates the app and configures it
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = ''
        DATABASE = os.path.join(app.instnace_path, 'Templaholic.mySQL'),)
    
    if test_config is None:
        #Loads the instance for the app if it exist when its not testing
        app.config.frompyfile('config.py', silent=True)
    else:
        #Load the test config if passed into
        app.config.from_mapping(test_config)
        
    #ensurance of the isntance folder that exists
    try:
        os.maredirs(app.instance_path)
    except OSError:
        pass """