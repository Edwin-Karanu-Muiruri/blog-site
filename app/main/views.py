from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Quote
from .forms import UpdateProfile,CommentForm,BloggingForm
from .. import db
from . import main
from ..requests import get_quote


#application views
@main.route('/')
def index():
    '''
    Root page view function that returns the index page and its data
    '''
    title = 'Blog Spot'
    quote = get_quote()
    blogs = Blog.query.all()
    return render_template('index.html',title=title,quote = quote, blogs=blogs)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    blogs = Blog.query.filter_by(user_id = user.id).order_by(Blog.posted.desc())
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,blogs=blogs)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form,user=user)

@main.route('/user/<uname>/blog',methods= ['GET','POST'])
@login_required
def new_blog(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = BloggingForm()
    blog = Blog()

    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        blog.user_id = current_user.id


        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))

    return render_template('new_blog.html',uname = uname, user = user, BloggingForm = form)


@main.route('/user/<uname>/delete/<id>/blog')
@login_required
def del_blog(uname, blog_id):
    user = User.query.filter_by(username = uname).first()
    blogs = Blog.query.filter_by(user_id = user.id).order_by(Blog.posted.desc())
    blog = Blog.query.filter_by(id = blog_id).first()

    if blog.user_id == current_user.id:
        blog.delete_blog()

    return render_template("profile/profile.html", user = user, blogs = blogs)

@main.route('/comments/<blog_id>/new', methods = ['GET', 'POST'])
@login_required
def new_comment(blog_id):
    form = CommentForm()
    blog = Blog.query.filter_by(id = blog_id).first()
    comment = Comment()

    if form.validate_on_submit():
        comment.comment = form.comment.data
        comment.blog_id = blog.id
        comment.user_id = current_user.id

        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('main.comments', blog_id=blog.id ))

    return render_template('new_comment.html', comment_form = form)


@main.route('/comments/<blog_id>')
@login_required
def comments(blog_id):
    blog = Blog.query.filter_by(id = blog_id).first()
    comments = Comment.query.filter_by(blog_id = blog.id).order_by(Comment.posted.desc())


    return render_template('comments.html', blog = blog, comments = comments)


@main.route('/comment/delete/<blog_id>/<comment_id>')
@login_required
def del_comment(blog_id, comment_id):
    blog = Blog.query.filter_by(id = blog_id).first()
    comments = Comment.query.filter_by(blog_id = blog.id).order_by(Comment.posted.desc())
    comment = Comment.query.filter_by(id = comment_id).first()
    if blog.user_id == current_user.id or comment.user_id == current_user.id:

        Comment.delete_comment(comment)

    return render_template('comments.html', blog = blog, comments = comments)



