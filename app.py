import os
import datetime
from os import path
from flask import Flask, render_template, request, redirect, url_for, flash, session


app = Flask(__name__)
app.config.update(
    SECRET_KEY = os.environ.get('SECRET_KEY')
)


# Static page routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')
    

@app.route('/joinus')
def joinus():
    return render_template('joinus.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registercompany')
def registercompany():
    return render_template('registercompany.html')

# Error Handling of 404 & 500
@app.errorhandler(404)
def response_404(exception):
    return render_template('404.html', exception=exception)


@app.errorhandler(500)
def response_500(exception):
    return render_template('500.html', exception=exception)


if __name__ == "__main__":
    app.run(
        host = os.environ.get('IP', '127.0.0.1'),
        port = os.environ.get('PORT', '5000'),
        debug=True
    )