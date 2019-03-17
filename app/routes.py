#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-
# View Functions for mapping URLs to Handlers

import sys
if sys.platform == 'darwin':
    sys.path.insert(0, "/Users/chenhuming/workspace/faqrepo/venv/lib/python3.7/site-packages")
else:
    sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, \
ResetPasswordForm, NewPostForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post
from werkzeug.urls import url_parse
from app.mail import send_password_reset_email


@app.route('/')
@app.route('/index')
# @login_required
def index():
    posts = Post.query.all()
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # validate form data
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    # render form
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    # validate form data
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    # render form
    return render_template('register.html', title='Register', form=form)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    # validate form data
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    # render form
    return render_template('reset_password_request.html', title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    # validate form data
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    # render form
    return render_template('reset_password.html', form=form)


@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = NewPostForm()
    # validate form data
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Congratulations, you have created a new post!')
        return redirect(url_for('index'))
    # render form
    return render_template('new_post.html', title='New Post', form=form)


@app.route('/view_post/<int:id>')
def view_post(id):
    post = Post.query.filter_by(id=id).first()
    if post:
        return render_template('view_post.html', title='View Post', post=post)
    else:
        return redirect(url_for('index'))


@app.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        return 'Error loading #{id}'.format(id=id)
    form = NewPostForm(obj=post)
    # validate form data
    if request.method == 'POST' and form.validate():
        post.title = form.title.data
        post.body = form.body.data
        db.session.commit()
        flash('Post updated successfully!')
        return redirect(url_for('view_post', id=post.id))
    # render form
    return render_template('edit_post.html', title='Edit Post', form=form)


@app.route('/delete_post/<int:id>')
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if post:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfully!')
    return redirect(url_for('index'))
