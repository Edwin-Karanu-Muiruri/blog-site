from flask import render_template
from . import authentication
from ..models import User
from .forms import SignUpForm,LoginForm
from flask_login import login_user
from .. import db

@authentication.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Log in"
    return render_template('auth/login.html',login_form=login_form,title=title)

@authentication.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('authentication.login'))
        title = "Sign Up"
    return render_template('auth/signup.html',signup_form = form,title=title)

