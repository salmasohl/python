from flask import Blueprint, render_template, request, flash, jsonify


views = Blueprint('views', __name__)

@views.route('/')
def entree():
    return render_template("entree.html")

@views.route('/login')
def login():
    return render_template("login.html")



