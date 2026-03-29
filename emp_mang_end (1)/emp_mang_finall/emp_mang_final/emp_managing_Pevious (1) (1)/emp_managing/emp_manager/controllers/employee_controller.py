from flask import render_template, request, redirect, url_for, flash ,jsonify 
from models.employee_model import Employee
from models import db
from datetime import datetime
from sqlalchemy import or_

def manage_employees():
    employees = Employee.query.all()
    return render_template("manage_employee.html", employees=employees)


def add_employee():
    if request.method == "POST":
        dob_str = request.form.get("dob")
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date() if dob_str else None

        emp = Employee(
            first_name=request.form["first_name"],
            middle_name=request.form.get("middle_name", ""),
            last_name=request.form["last_name"],
            gender=request.form["gender"],
            dob=dob,   
            mobile_number=request.form["mobile_number"],
            alternate_mobile_number=request.form.get("alternate_mobile_number", ""),
            email=request.form["email"],
            marital_status=request.form["marital_status"],
            blood_group=request.form["blood_group"],
            branch=request.form["branch"]

        )
        
    
        db.session.add(emp)
        db.session.commit()
        flash("Employee added successfully!", "success")
        return redirect(url_for("manage_employees"))

    return render_template("add_employee.html")



def view_employee(id):
    emp = Employee.query.get_or_404(id)
    return render_template("view_employee.html", emp=emp)


def delete_employee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    flash(f"Employee '{emp.first_name}' deleted successfully!", "success")
    return redirect(url_for("manage_employees"))


def edit_employee(id):
    emp = Employee.query.get_or_404(id)

    if request.method == "POST":
        dob_str = request.form.get("dob")
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date() if dob_str else None

        emp.first_name = request.form["first_name"]
        emp.middle_name = request.form.get("middle_name", "")
        emp.last_name = request.form["last_name"]
        emp.gender = request.form["gender"]
        emp.dob = dob   
        emp.mobile_number = request.form["mobile_number"]
        emp.alternate_mobile_number = request.form.get("alternate_mobile_number", "")
        emp.email = request.form["email"]
        emp.marital_status = request.form["marital_status"]
        emp.blood_group = request.form["blood_group"]
        emp.branch = request.form["branch"]



        db.session.commit()
        flash(f"Employee '{emp.first_name}' updated successfully!", "success")
        return redirect(url_for("manage_employees"))

    return render_template("edit_employee.html", emp=emp)





def employees_data():
    
    draw = int(request.args.get("draw", 1))
    start = int(request.args.get("start", 0))
    length = int(request.args.get("length", 10))
    search_value = request.args.get('search[value]')

    query = Employee.query

    
    if search_value:
        query = query.filter(
            or_(
                Employee.first_name.ilike(f"%{search_value}%"),
                Employee.mobile_number.ilike(f"%{search_value}%"),
                Employee.email.ilike(f"%{search_value}%"),
                Employee.branch.ilike(f"%{search_value}%")
            )
        )

    
    records_filtered = query.count()
    records_total = Employee.query.count()

    
    employees = query.offset(start).limit(length).all()

    
    data = []
    for i, emp in enumerate(employees, start=1 + start):
        data.append({
            "view": f'<a href="/employees/view/{emp.id}"><i class="bi bi-eye"></i></a>',
            "index": i,
            "first_name": emp.first_name,
            "mobile_number": emp.mobile_number,
            "email": emp.email,
            "branch": emp.branch,
            "edit": f'<a href="/employees/edit/{emp.id}"><i class="bi bi-pencil"></i></a>',
            "delete": f'<a href="/employees/delete/{emp.id}"><i class="bi bi-trash"></i></a>'
        })

    return jsonify({
        "draw": draw,
        "recordsTotal": records_total,
        "recordsFiltered": records_filtered,
        "data": data
    })