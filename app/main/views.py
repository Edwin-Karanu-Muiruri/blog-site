from flask import render_template,request,redirect,url_for,abort
#from app import app
from flask_login import login_required
from ..models import User

#application views
#@main.route('/')
def index():
    '''
    Root page view function that returns the index page and its data
    '''
    return render_template('home.html')

#@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
