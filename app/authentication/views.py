from flask import render_template
from . import authentication
from ..models import User
from .forms import SignUpForm
from .. import db

@authentication.route('/login')
def login():
    return render_template('authentication/login.html')

@authentication.route('/signup', methods = ["GET","POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('authentication.login'))
        title = "Sign Up"
    return render_template('authentication/signup.html',signup_form = form)