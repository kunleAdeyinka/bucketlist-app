################################################################################
############################## imports #########################################
################################################################################

from flask import flash, redirect, render_template, request, url_for, Blueprint, g
from flask.ext.login import login_user, login_required, logout_user, current_user
from form import LoginForm, RegisterForm
from project import db
from project.models import User, bcrypt


################################################################################
############################## config ##########################################
################################################################################
users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


################################################################################
############################## routes  #########################################
################################################################################

@users_blueprint.before_request
def get_current_user():
    g.user = current_user
    
    
@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.welcome'))
    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                #session['logged_in'] = True
                login_user(user)
                flash('You are now logged in!')
                return redirect(url_for('home.welcome'))
            else:
                 error = 'Invalid credentials. Please try again.'
    return render_template('login.html', form=form, error=error)
  
    
@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are now logged out!')
    return redirect(url_for('home.welcome'))
    

