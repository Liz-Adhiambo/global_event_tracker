from flask import render_template, url_for, flash, redirect,request
from event_tracker import app
from event_tracker.forms import RegistrationForm, LoginForm
from event_tracker.models import User, Post
from event_tracker.news import get_gdelt_data
import pandas as pd
import requests

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
API_URL = "https://api.gdeltproject.org/api/v2/doc/doc"
API_KEY='pub_27092853c6eab6081ead2dce47bcf3adce0ec'

@app.route("/")
@app.route("/home")
def home():

    posts=requests.get('https://newsdata.io/api/1/news?apikey=pub_27092853c6eab6081ead2dce47bcf3adce0ec&q=sport')
    posts=posts.json()
    news=posts['results']
    print(posts['results'])

    return render_template('home.html', news=news)

@app.route("/news", methods=["GET"])
def get_news():
    global_news = get_gdelt_data()
    global_news=global_news['data'][0]['toparts']

   
    return render_template("new.html", articles=global_news)




@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)