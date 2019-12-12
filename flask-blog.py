from dotenv import load_dotenv
import os
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistationForm, LoginForm

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

posts = [
    {
        'author': 'Emilian',
        'title': 'Blog Post Title',
        'content': 'dsadas dsad asda dasdasda',
        'date_posted' : '11 December 2019'
    },
    
    {
        'author': 'Ognianov',
        'title': 'New Post',
        'content': 'hello this is my blog',
        'date_posted': '10 December 2019'
    },
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About us')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@admin.com' and form.password.data=="123":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Loggin failed!', 'danger')
    return render_template('login.html', title='Login', form=form)