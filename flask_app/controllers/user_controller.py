from flask import render_template, redirect, request
from flask_app import app

from flask_app.models.users_model import User


@app.route('/')
def all_users():

    return render_template("readall.html", users=User.get_all())

@app.route('/users/new')
def new_company():
    return render_template("create.html")

@app.route('/users/create', methods=['POST'])
def create_company():
    User.create(request.form)
    return redirect('/')