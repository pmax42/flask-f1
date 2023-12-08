from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Driver(db.Model):
    __tablename__ = 'drivers'
    driverId = db.Column(db.Integer, primary_key=True)
    driverRef = db.Column(db.String(255))
    constructor_id = db.Column(db.Integer, db.ForeignKey('constructors.constructorId'))
    number = db.Column(db.Integer)
    code = db.Column(db.String(3))
    forename = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    dob = db.Column(db.Date)
    nationality = db.Column(db.String(255))
    url = db.Column(db.String(255))

class Constructor(db.Model):
    __tablename__ = 'constructors'
    constructorId = db.Column(db.Integer, primary_key=True)
    constructorRef = db.Column(db.String(255))
    name = db.Column(db.String(255))
    nationality = db.Column(db.String(255))
    url = db.Column(db.String(255))
    color = db.Column(db.String(7))
    image_url = db.Column(db.String(255))
    foundation_year = db.Column(db.Integer)
    team_director = db.Column(db.String(255))
    logo = db.Column(db.String(255))
    country_iso = db.Column(db.String(3))
    championships_won = db.Column(db.Integer)
    drivers = db.relationship('Driver', backref='constructor')

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone_number = db.Column(db.String(10))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())