# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, ValidationError
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField, DateTimeField, DateField, FloatField

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
    unionname = StringField('Union Name', validators=[DataRequired()])
    branchname = StringField('Branch Name', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    industry = StringField('Industry', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=[('AL', 'AL'), ('AK', 'AK'), ('AS', 'AS'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('DC', 'DC'), ('FL', 'FL'), ('GA', 'GA'), ('GU', 'GU'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NI', 'NI'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('MP', 'MP'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('PR', 'PR'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('VI', 'VI'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')])
    zipcode = IntegerField('Zipcode', validators=[DataRequired()])
    lat = FloatField('Latitude', validators=[DataRequired()])
    lon = FloatField('Longitude', validators=[DataRequired()])
    #unionized = BooleanField('Have you unionized?', validators=[DataRequired()])
    unionizedate = DateField('Date unionized (YYYY-MM-DD)', validators=[DataRequired()])
    unionrep = StringField('Name of union rep', validators=[DataRequired()])
    conemail = StringField('Contact Email', validators=[DataRequired(), Email()])
    conpnumber = IntegerField('Contact Phone Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

class WorkplaceForm(FlaskForm):
    branchname = StringField('Workplace Name', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    industry = StringField('Industry', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=[('AL', 'AL'), ('AK', 'AK'), ('AS', 'AS'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('DC', 'DC'), ('FL', 'FL'), ('GA', 'GA'), ('GU', 'GU'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NI', 'NI'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('MP', 'MP'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('PR', 'PR'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('VI', 'VI'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')])
    zipcode = IntegerField('Zipcode', validators=[DataRequired()])
    lat = FloatField('Latitude', validators=[DataRequired()])
    lon = FloatField('Longitude', validators=[DataRequired()])
    #unionized = BooleanField('Have you unionized?', validators=[DataRequired()])
    conemail = StringField('Contact Email', validators=[DataRequired(), Email()])
    conpnumber = IntegerField('Contact Phone Number', validators=[DataRequired()])
    submit = SubmitField('Submit')