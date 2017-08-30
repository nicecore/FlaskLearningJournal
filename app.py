from flask import (Flask, g, render_template, flash, redirect, url_for,
                    abort)
from flask_bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, 
                        logout_user, login_required, current_user)
import forms
import models

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"

app = Flask(__name__)
app.secret_key = 'sadijweoirf9347yr0wqdfhuqibduafwe'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """Connect to database before each request and set g.user to current_user"""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close database connection after each request"""
    g.db.close()
    return response


# Initialize database, create database tables and run Flask app
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)