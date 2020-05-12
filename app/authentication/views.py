from flask import render_template,redirect,url_for,request,flash
from . import authentication
from ..models import User
from .forms import SignUpForm,LoginForm
from flask_login import login_user,logout_user,login_required
from .. import db
from .. import main

@authentication.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    
    return render_template('auth/login.html',login_form=login_form)

@authentication.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('authentication.login'))
        
    return render_template('auth/signup.html',signup_form = form)

@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for("main.index"))#make this work