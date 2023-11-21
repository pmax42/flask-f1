from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
import os

load_dotenv()

db = SQLAlchemy()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    init_db(app)

    return app

def init_db(app):
    # Check database connection
    engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}')
    try:
        engine.connect()
        # Try a select on drivers table
        with engine.connect() as con:
            rs = con.execute(text("SELECT * FROM drivers"))
            for row in rs:
                print(row)
        print('Database connected')
    except:
        print('Database connection failed')
        return