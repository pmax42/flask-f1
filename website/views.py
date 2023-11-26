from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Constructor
from . import db
from .forms import UpdateAccountForm

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    # Query all constructors of 2023 season
    constructors = Constructor.query.filter(Constructor.color != None).all()
    return render_template("home.html", user=current_user, constructors=constructors)

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm(request.form)

    # Populate form with current user data
    if request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        # Print form data
        print(form.data)

    if request.method == 'POST':
        if form.validate_on_submit():
            current_user.email = request.form.get('email')
            current_user.first_name = request.form.get('first_name')
            current_user.last_name = request.form.get('last_name')
            # Save changes to database
            db.session.commit()
            flash("Changes saved!", category='success')
        else:
            first_error = list(form.errors)[0]
            flash(form.errors[first_error][0], category='error')

    return render_template("profile.html", form=form)