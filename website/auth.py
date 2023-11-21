from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout', methods=['POST'])
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        firstName = request.form.get('first_name')
        lastName = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
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
            flash("Account created", category='success')

    return render_template("sign-up.html")