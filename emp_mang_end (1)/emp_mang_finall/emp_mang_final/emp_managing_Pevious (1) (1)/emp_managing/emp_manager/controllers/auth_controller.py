from flask import render_template, request, redirect, url_for, session
from models import User
from models import db

def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session["user"] = username
            return redirect(url_for("manage_employees"))
        else:
            return "Invalid Username or Password"

    return render_template("login.html")


def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(username=username, email=email, password=password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))   

    return render_template("register.html")


def logout():

    session.clear()
    return redirect(url_for("login"))