from flask import Flask, redirect, url_for
from config import Config
from models import db
from controllers import employee_controller
from controllers import auth_controller

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # ---------------------------
    # AUTH ROUTES
    # ---------------------------

    app.add_url_rule("/", "login",
        auth_controller.login, methods=["GET","POST"])

    app.add_url_rule("/login", "login_page",
        auth_controller.login, methods=["GET","POST"])

    # ✅ REGISTER ROUTE ADD KIYA
    app.add_url_rule("/register", "register",
        auth_controller.register, methods=["GET","POST"])

    app.add_url_rule("/logout", "logout",
        auth_controller.logout)

    # ---------------------------
    # EMPLOYEE ROUTES
    # ---------------------------
# ---------------------------
# EMPLOYEE ROUTES
# ---------------------------

    app.add_url_rule("/employees", "manage_employees",
    employee_controller.manage_employees)

    app.add_url_rule("/employees/add", "add_employee",
    employee_controller.add_employee, methods=["GET","POST"])

    app.add_url_rule("/employees/view/<int:id>", "view_employee",
    employee_controller.view_employee)

    app.add_url_rule("/employees/delete/<int:id>", "delete_employee",
    employee_controller.delete_employee, methods=["GET","POST"])

    app.add_url_rule("/employees/edit/<int:id>", "edit_employee",
    employee_controller.edit_employee, methods=["GET","POST"])

# ✅ DATATABLES AJAX ROUTE
    app.add_url_rule("/employees_data", "employees_data",
    employee_controller.employees_data)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)