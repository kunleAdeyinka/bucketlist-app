################################################################################
#################### imports ###################################################
from project import app, db
from project.models import BlogPost
from flask import render_template, url_for, request, redirect, session, flash, g, Blueprint
from functools import wraps
import os


################################################################################
############################## config ##########################################
home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################################################################################
#################### helper functions ##########################################

# Login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('users.login'))
    return wrap



################################################################################
#################### routes ####################################################

@home_blueprint.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)

@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html")
 
