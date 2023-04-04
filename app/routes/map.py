from app import app
from app.utils.secrets import getSecrets
import requests
from flask import render_template, flash, redirect, url_for
import requests
from flask_login import current_user
from app.classes.data import Clinic
from app.classes.forms import ClinicForm
from flask_login import login_required
import datetime as dt

@app.route('/map/map')
def clinicMap():

    clinics = Clinic.objects()

    return render_template('cliniclocator.html',clinics=clinics)