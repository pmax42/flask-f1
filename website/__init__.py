from dotenv import load_dotenv
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os
from flask_login import LoginManager
from .helpers import snake_case
# from .tables import test_get_data

load_dotenv()

db = SQLAlchemy()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def create_app():
    app = Flask(__name__)

    @app.before_request
    def check_redirect():
        # Check if the request is a redirect
        if request.referrer and request.referrer.endswith(request.url) and request.method != 'POST':
            print('MIDDLEWARE: Redirect detected')
            # This is a redirect to the same page, cancel it
            return make_response('', 204)

    app.jinja_env.filters['snake_case'] = snake_case
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    init_db(app)
    # test_get_data(db) # TODO - Remove this

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def init_db(app):
    # Check database connection
    engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}')
    try:
        engine.connect()
        print('Database connected')
    except:
        print('Database connection failed')
        return