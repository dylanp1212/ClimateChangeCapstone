from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Union
from app.classes.forms import UnionForm
from app.classes.data import Workplace
from app.classes.forms import WorkplaceForm
from flask_login import login_required
import datetime as dt


@app.route('/union/new', methods=['GET', 'POST'])
@login_required
def unionNew():
    form = UnionForm()
    if form.validate_on_submit():
  
        newUnion = Union(
            unionname = form.unionname.data,
            branchname = form.branchname.data,
            company = form.company.data,
            industry = form.industry.data,
            bio = form.bio.data,
            address = form.address.data,
            city = form.city.data,
            state = form.state.data,
            zipcode = form.zipcode.data,
            lat = form.lat.data,
            lon = form.lon.data,
            unionizedate = form.unionizedate.data,
            unionrep = form.unionrep.data,
            conemail = form.conemail.data,
            conpnumber = form.conpnumber.data,
            author = current_user.id,
            modifydate = dt.datetime.utcnow,
        )
        newUnion.save()

        #return redirect(url_for('union',unionID=newUnion.id))
        return redirect('new')
    return render_template('unionform.html',form=form)

@app.route('/workplace/new', methods=['GET', 'POST'])
@login_required
def workplaceNew():
    form = WorkplaceForm()
    if form.validate_on_submit():
  
        newWorkplace = Workplace(
            branchname = form.branchname.data,
            company = form.company.data,
            industry = form.industry.data,
            bio = form.bio.data,
            address = form.address.data,
            city = form.city.data,
            state = form.state.data,
            zipcode = form.zipcode.data,
            lat = form.lat.data,
            lon = form.lon.data,
            conemail = form.conemail.data,
            conpnumber = form.conpnumber.data,
            author = current_user.id,
            modifydate = dt.datetime.utcnow,
        )
        newWorkplace.save()

        #return redirect(url_for('union',unionID=newUnion.id))
        return redirect('new')
    return render_template('workplaceform.html',form=form)

@app.route('/union/display/<unionid>', methods=['GET', 'POST'])
@login_required
def displayUnion(unionid):
    display = Union.objects.get(id=unionid)
    return render_template('uniondisplay.html',union=display)

@app.route('/workplace/display/<workplaceid>', methods=['GET', 'POST'])
@login_required
def displayWorkplace(workplaceid):
    display = Workplace.objects.get(id=workplaceid)
    return render_template('workplacedisplay.html',workplace=display)

@app.route('/union/all', methods=['GET', 'POST'])
@login_required
def displayAllUnions():
    unions = Union.objects()
    return render_template('unionall.html', unions=unions)

@app.route('/workplace/all', methods=['GET', 'POST'])
@login_required
def displayAllWorkplace():
    workplaces = Workplace.objects()
    return render_template('workplaceall.html', workplaces=workplaces)

@app.route('/map', methods=['GET', 'POST'])
@login_required
def map():
    unions = Union.objects()
    workplaces = Workplace.objects()
    return render_template('map.html', unions=unions, workplaces=workplaces)