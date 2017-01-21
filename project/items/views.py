################################################################################
############################## imports #########################################
################################################################################
import os
import uuid
from flask import flash, redirect, render_template, request, url_for, Blueprint, g
from flask.ext.login import login_user, login_required, logout_user, current_user
from form import BucketItemForm
from project import db, UPLOAD_FOLDER
from project.models import User, BucketItem, Like
from werkzeug.utils import secure_filename


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
        image_file = form.photo.data
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(UPLOAD_FOLDER, filename))
        unique_name = UPLOAD_FOLDER + '/' + filename
        staticFolder = unique_name.find('static')
        path = unique_name[staticFolder:]
        path = '/' + path
        bucket_item = BucketItem(title=form.title.data, description=form.description.data, author_id=g.user.id, is_private=form.private.data, is_done=form.done.data, photo_path=path)
        db.session.add(bucket_item)
        db.session.flush()
        like = Like( bucketitem_id=bucket_item.id, user_id=g.user.id, likes=0)
        db.session.add(like)
        db.session.commit()
        flash('New item was successfully posted. Thanks.')
        return redirect(url_for('home.welcome'))
    return render_template('item.html', form=form)


@items_blueprint.route('/editItem/<int:bucketitem_id>/edit/', methods=['GET', 'POST'])
@login_required
def editItem(bucketitem_id):
    editedItem = db.session.query(BucketItem).filter_by(id=bucketitem_id).one()
    
    form = BucketItemForm(obj=editedItem)
    
    if form.validate_on_submit():
        form.populate_obj(editedItem)
        db.session.commit()
        return redirect(url_for('home.welcome'))
    else:
        return render_template('editItem.html', form=form, bucketitem=editedItem) 
            
            
    
    

@items_blueprint.route('/deleteItem/<int:bucketitem_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteItem(bucketitem_id):
    deletedBucketitem = db.session.query(BucketItem).filter_by(id = bucketitem_id).one()
    form = BucketItemForm(obj=deletedBucketitem)
    if request.method == 'POST':
        db.session.delete(deletedBucketitem)
        db.session.commit()
        return redirect(url_for('home.welcome'))
    return render_template('deleteItem.html', form = form, bucketitem=deletedBucketitem)
    
