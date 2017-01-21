################################################################################
#################### imports ###################################################
import math

from project import db
from project import POSTS_PER_PAGE
from project.models import BucketItem, Like
from flask import render_template, url_for, request, redirect, session, flash, g, Blueprint, json
from flask.ext.login import login_required, current_user


################################################################################
############################## config ##########################################
home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################################################################################
#################### routes ####################################################
@home_blueprint.before_request
def get_current_user():
    g.user = current_user
    

@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@home_blueprint.route('/welcome', methods=['GET', 'POST'])
@home_blueprint.route('/welcome/<int:page>', methods=['GET', 'POST'])
@login_required
def welcome(page=1):
    bucketitems = BucketItem.query.filter(BucketItem.is_private==False).order_by(BucketItem.timestamp.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template("welcome.html", bucketitems=bucketitems)


@home_blueprint.route('/addUpdateLike', methods=['POST'])  
@login_required
def addUpdateLike():
    bucketitem_id = request.form['bucket_item']
    like = request.form['like']
    user_id = g.user.id
    likes_list = db.session.query(Like).filter_by(bucketitem_id=bucketitem_id, user_id=user_id).first()
    if likes_list is None:
        print 'none'
        likes_list = Like(bucketitem_id, user_id, like)
        db.session.add(likes_list)
        db.session.commit()
    elif likes_list.likes > 1 and likes_list.user_id == user_id:
        print '>1'
        like_count = likes_list.likes
        likes_list.likes = like_count - 1
        db.session.flush()
    elif likes_list.likes == 1 and likes_list.user_id == user_id:
        print '==1'
        likes_list.likes = 0
        db.session.flush()
    else:
        print 'else'
        print like
        print bucketitem_id
        like_list = Like(bucketitem_id, user_id, like)
        db.session.add(likes_list)
        db.session.flush()
    
   
    return json.dumps({'status':'OK', 'total':likes_list.likes, 'spId':likes_list.bucketitem_id})
    
    
        
        
        
        
            
    

 
