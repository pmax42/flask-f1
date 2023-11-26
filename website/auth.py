from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password1):
                flash("Logged in successfully", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password", category='error')
        else:
            flash("Email does not exist", category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        firstName = request.form.get('first_name')
        lastName = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category='error')
        elif len(email) < 5:
            flash("Email must be greater than 5 characters", category='error')
        elif len(phone_number) < 10:
            flash("Phone number must be equal to 10 characters", category='error')
        elif len(firstName) < 3:
            flash("First name must be greater than 2 characters", category='error')
        elif len(lastName) < 3:
            flash("Last name must be greater than 2 characters", category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        elif len(password1) < 8:
            flash("Password must be at least 8 characters", category='error')
        else:
            new_user = User(
                email=email, 
                phone_number=phone_number, 
                first_name=firstName, 
                last_name=lastName, 
                password=generate_password_hash(password1)
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created", category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    return render_template("sign-up.html", user=current_user)