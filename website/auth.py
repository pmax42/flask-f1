from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .forms import RegistrationForm, LoginForm
from .helpers import snake_to_normal

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form.get('email').lower()
            password = request.form.get('password')

            # Check if user exists
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash("Logged in successfully", category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash("Incorrect password", category='error')
            else:
                flash("Email does not exist", category='error')
        else:
            key, message_list = list(form.errors.items())[0]
            message = message_list[0]
            flash(snake_to_normal(key) + ': ' + message, category='error')

    return render_template("login.html", form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    form = RegistrationForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form.get('email').lower()
            phone_number = request.form.get('phone_number')
            firstName = request.form.get('first_name').title()
            lastName = request.form.get('last_name').capitalize()
            password = request.form.get('password')

            new_user = User(
                email=email, 
                phone_number=phone_number, 
                first_name=firstName, 
                last_name=lastName, 
                password=generate_password_hash(password)
            )

            db.session.add(new_user)
            db.session.commit()
            flash("Account created", category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
        else:
            key, message_list = list(form.errors.items())[0]
            message = message_list[0]
            flash(snake_to_normal(key) + ': ' + message, category='error')
    return render_template("sign-up.html", form=form)
