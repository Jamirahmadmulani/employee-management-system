
import os

class Config:
    SECRET_KEY = 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/emp_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
