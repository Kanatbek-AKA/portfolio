import flask
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy, Pagination
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

# Going to add it later
# from flask_bootstrap import Bootstrap


app = Flask(__name__, template_folder="templates", static_folder="static")


# SQLAlchemy
# app.config["SECRET_KEY"] = 'Secret Keys'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///some.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# Creating classes to define DB modul 
# in process....
#


# 
@app.route('/')
def home() :
    """features to add"""
    return render_template("index.html")


@app.route('/about/')
def about() :
    """features to add"""
    return render_template('about.html')


@app.route('/skills/', methods=['GET', 'POST'])
def skills() :
    """features to add"""
    return render_template('skills.html' )


@app.route('/contact/' ,  methods=['GET', 'POST'])
def contact() :
    """features to add"""
    return render_template("contact.html")



# Thinking ....
def geolocation(api, *args, **kwargs):
    pass

# Thinking ....
def ip_detect(api, *args, **kwargs) :
    pass



# 
if __name__ == "__main__":
    print(app.run(debug = True))
