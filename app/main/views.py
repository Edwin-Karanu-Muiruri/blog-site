from flask import render_template
#from app import app
from flask_login import login_required

#application views
#@app.route('/')
def index():
    '''
    Root page view function that returns the index page and its data
    '''
    return render_template('home.html')