# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, ValidationError
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField, DateTimeField

def zipCodeCheck(form, field):
    if len(field.data) > 5 or len(field.data) < 5:
        raise ValidationError('Invalid Zipcode')
    
def pNumCheck(form, field):
    if len(field.data) > 10 or len(field.data) < 10:
        raise ValidationError('Invalid Phone Number')

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image")
    role = SelectField('Role',choices=[("Teacher","Teacher"),("Student","Student")])
    pnumber = IntegerField('Phone Number',validators=[DataRequired()]) 
    submit = SubmitField('Post')
    

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ClinicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    streetAddress = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UnionForm(FlaskForm):
    name = StringField('Name of Workplace', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    industry = StringField('Industry', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = IntegerField('Zipcode', validators=[DataRequired(), zipCodeCheck])
    lat = IntegerField('Latitude', validators=[DataRequired()])
    lon = IntegerField('Longitude', validators=[DataRequired()])
    unionized = BooleanField('Have you unionized?', validators=[DataRequired()])
    unionname = StringField('Union Name', validators=[DataRequired()])
    unionizedate = DateTimeField('Date unionized', validators=[DataRequired()])
    unionrep = StringField('Name of union rep', validators=[DataRequired()])
    conemail = StringField('Contact Email', validators=[DataRequired(), Email()])
    conpnumber = IntegerField('Contact Phone Number', validators=[DataRequired(), pNumCheck])
    submit = SubmitField('Submit')