from flask import Blueprint, render_template, redirect, url_for

pages = Blueprint('main', __name__)

@pages.route('/')
def index():
    return render_template('index.html')

@pages.route('/profile')
def profile():
    return render_template('profile.html')

@pages.route('/login')
def login():
    return render_template('login.html')

# @pages.route('/login', methods=['POST'])
# def login_post():

@pages.route('/signup')
def signup():
    return render_template('sign.html')

# @pages.route('/signup', methods=['POST'])
# def signup_post():

@pages.route('/logout')
def logout():
    return redirect(url_for('index'))
