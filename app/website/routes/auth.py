from flask import Blueprint, render_template, request, flash, jsonify


auth = Blueprint('auth', __name__)



@auth.route('/forgot', methods=['GET', 'POST'])
def forgot():
    return render_template("forgot.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


        

            





