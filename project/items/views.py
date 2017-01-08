################################################################################
############################## imports #########################################
################################################################################

from flask import flash, redirect, render_template, request, url_for, Blueprint, g
from flask.ext.login import login_user, login_required, logout_user, current_user
from form import BucketItemForm
from project import db
from project.models import User, BucketItem


################################################################################
############################## config ##########################################
################################################################################
items_blueprint = Blueprint(
    'items', __name__,
    template_folder='templates'
)


################################################################################
############################## routes  #########################################
################################################################################

@items_blueprint.before_request
def get_current_user():
    g.user = current_user
    

@items_blueprint.route('/addItem', methods=['GET', 'POST'])
@login_required
def addItem():
    form = BucketItemForm()
    if form.validate_on_submit():
        bucket_item = BucketItem(title=form.title.data, post=form.post.data, author_id=g.user.id)
        db.session.add(bucket_item)
        db.session.commit()
        flash('New item was successfully posted. Thanks.')
        return redirect(url_for('home.welcome'))
    return render_template('item.html', form=form)
    
