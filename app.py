import os
from flask import Flask, render_template, url_for, request, redirect, session, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
import sqlite3


app = Flask(__name__)
app.secret_key = "tdfknfknfkneoerebeobrebrobdfnldnfadnfdfna;ndfkanfseren"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# create the sqlachemy object
db = SQLAlchemy(app)

from models import *

# Login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    posts = []
    try:
        # return "Hello, world" # return a string
        g.db = connect_db()
        cur = g.db.execute('select * from posts')
        
        for row in cur.fetchall():
            posts.append(dict(title=row[0], description=row[1]))
            
        g.db.close()
    except sqlite3.OperationalError:
        flash("You have no database")
    return render_template("index.html", posts=posts)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You are now logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
 
 
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You are now logged out!')
    return redirect(url_for('welcome'))
    

def connect_db():
   return sqlite3.connect('posts.db')

if __name__ == '__main__':
     app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True)