################################################################################
#################### imports ###################################################
from .forms import MessageForm
from project import db
from project.models import BlogPost
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
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(form.title.data, form.description.data, current_user.id)
        db.session.add(new_message)
        db.session.commit()
        flash('New post was successfully posted. Thanks.')
        return redirect(url_for('home.home'))
    else:
        return render_template("index.html", form=form, error=error)

@home_blueprint.route('/welcome')
@login_required
def welcome():
    posts = db.session.query(BlogPost).all()
    return render_template("welcome.html", posts=posts)
 
