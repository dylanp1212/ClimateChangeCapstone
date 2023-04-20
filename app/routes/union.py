from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Union
from app.classes.forms import UnionForm
from flask_login import login_required
import datetime as dt

# These routes and functions are for accessing and editing user profiles.

# The first line is what listens for the user to type 'myprofile'
@app.route('/union/new', methods=['GET', 'POST'])
@login_required
def unionNew():
    form = UnionForm()
    if form.validate_on_submit():
  
        newUnion = Union(
            subject = form.subject.data,
            content = form.content.data,
            tag = form.tag.data,
            author = current_user.id,
            # This sets the modifydate to the current datetime.
            modify_date = dt.datetime.utcnow
        )
        # This is a method that saves the data to the mongoDB database.
        newUnion.save()

        return redirect(url_for('union',unionID=newUnion.id))
    
    return render_template('unionform.html',form=form)