################################################################################
#################### imports ###################################################
from project import db
from project.models import BucketItem
from flask import render_template, url_for, request, redirect, session, flash, g, Blueprint
from flask.ext.login import login_required, current_user


################################################################################
############################## config ##########################################
home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################################################################################
#################### routes ####################################################

@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@home_blueprint.route('/welcome')
@login_required
def welcome():
    bucketitems = db.session.query(BucketItem).all()
    return render_template("welcome.html", bucketitems=bucketitems)
 
