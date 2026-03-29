from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .employee_model import Employee
from .employee_model import User