from flask import Flask, render_template, url_for

app = Flask(__name__)

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