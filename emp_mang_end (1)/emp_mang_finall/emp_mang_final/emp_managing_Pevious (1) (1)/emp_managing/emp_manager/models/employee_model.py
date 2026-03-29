from . import db

class Employee(db.Model):

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    dob = db.Column(db.Date)
    mobile_number = db.Column(db.String(15))
    alternate_mobile_number = db.Column(db.String(15))
    email = db.Column(db.String(100))
    marital_status = db.Column(db.String(20))
    blood_group = db.Column(db.String(5))
    branch = db.Column(db.String(100))


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(200))