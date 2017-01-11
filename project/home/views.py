################################################################################
#################### imports ###################################################
import math

from project import db
from project import POSTS_PER_PAGE
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

@home_blueprint.route('/welcome', methods=['GET', 'POST'])
@home_blueprint.route('/welcome/<int:page>', methods=['GET', 'POST'])
@login_required
def welcome(page=1):
    # db.session.query(BucketItem).paginate(page, POSTS_PER_PAGE, False)
    bucketitems = BucketItem.query.order_by(BucketItem.timestamp.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template("welcome.html", bucketitems=bucketitems)
 
