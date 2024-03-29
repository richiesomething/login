from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from .models import User
from . import db

pages = Blueprint('pages', __name__)

@pages.route('/')
def index():
    return render_template('index.html')

@pages.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@pages.route('/login')
def login():
    return render_template('login.html')

@pages.route('/login', methods=['POST'])
def login_post():
    email=request.form.get('email')
    password=request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Email or Password is incorrect')
        return redirect(url_for('pages.login'))

    login_user(user, remember=remember)
    return redirect(url_for('pages.profile'))

@pages.route('/signup')
def signup():
    return render_template('signup.html')

@pages.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists.')
        return redirect(url_for('pages.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('pages.login'))

@pages.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('pages.index'))
