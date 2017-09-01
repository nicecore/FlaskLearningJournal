"""Learning Journal, a Flask web app by Adam Cameron
for the Treehouse TechDegree"""

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

# Do we need the following stuff? Not if there's no user/logging in to do, correct?

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# @login_manager.user_loader
# def load_user(userid):
#     try:
#         return models.User.get(models.User.id == userid)
#     except models.DoesNotExist:
#         return None

@app.before_request
def before_request():
    """Connect to database before each request and set g.user to current_user"""
    g.db = models.DATABASE
    g.db.connect()
    # g.user = current_user


@app.after_request
def after_request(response):
    """Close database connection after each request"""
    g.db.close()
    return response

# Index/list of entries view
@app.route('/entries')
def list():
    stream = models.Entry.select().limit(100)
    return render_template('index.html', stream=stream)


# Details view
# Route for URL /detail followed by an entry's ID number
@app.route('/detail/<int:entry_id>')
def detail(entry_id):
    entry = models.Entry.get(models.Entry.id == entry_id)
    return render_template('detail.html', entry=entry)


@app.route('/new', methods=("GET", "POST"))
def new():
    form = forms.EntryForm()
    if form.validate_on_submit():
        models.Entry.create(
            title=form.title.data,
            timespent=form.timespent.data,
            what_learned=form.what_learned.data,
            resources=form.resources.data
        )
        flash("Entry posted! Thanks!", "success")
        return redirect(url_for('list'))        
    return render_template('new.html', form=form)


@app.route('/edit/<int:entry_id>', methods=("GET", "POST"))
def edit(entry_id):
    entry = models.Entry.get(models.Entry.id == entry_id)
    form = forms.EntryForm(obj=entry)
    if form.validate_on_submit():
        entry.title = form.title.data
        entry.timespent = form.timespent.data
        entry.what_learned = form.what_learned.data
        entry.resources = form.resources.data
        entry.save()
        return redirect(url_for('list'))
    return render_template('edit.html', form=form, entry=entry)


@app.route('/delete/<int:entry_id>')
def delete(entry_id):
    entry = models.Entry.get(models.Entry.id == entry_id)
    entry.delete_instance()
    flash("Entry deleted!", "success")
    return redirect(url_for('list'))





# Initialize database, create database tables and run Flask app
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)