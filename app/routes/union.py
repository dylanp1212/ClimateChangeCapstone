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
        flash('Union uploaded.')
        return redirect('all')
    return render_template('unionform.html',form=form, edit=0)

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
        flash('Workplace uploaded.')
        return redirect('all')
    return render_template('workplaceform.html', form=form, edit=0)

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

@app.route('/union/edit/<unionid>', methods=['GET', 'POST'])
@login_required
def unionEdit(unionid):
    form = UnionForm()
    if form.validate_on_submit():
        editUnion = Union.objects.get(id=unionid)
        editUnion.update(
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
        

        #return redirect(url_for('union',unionID=newUnion.id))
        flash('Union updated.')
        return redirect('/union/all')
    editUnion = Union.objects.get(id=unionid)    
    form.unionname.data = editUnion.unionname
    form.branchname.data = editUnion.branchname
    form.company.data = editUnion.company
    form.industry.data = editUnion.industry
    form.bio.data = editUnion.bio
    form.address.data = editUnion.address
    form.city.data = editUnion.city
    form.state.data = editUnion.state
    form.zipcode.data = editUnion.zipcode
    form.lat.data = editUnion.lat
    form.lon.data = editUnion.lon
    form.unionizedate.data = editUnion.unionizedate
    form.unionrep.data = editUnion.unionrep
    form.conemail.data = editUnion.conemail
    form.conpnumber.data = editUnion.conpnumber

    return render_template('unionform.html',form=form, edit=1)

@app.route('/workplace/edit/<workplaceid>', methods=['GET', 'POST'])
@login_required
def workplaceEdit(workplaceid):
    form = WorkplaceForm()
    if form.validate_on_submit():
        editWorkplace = Workplace.objects.get(id=workplaceid)
        editWorkplace.update(
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
        

        #return redirect(url_for('union',unionID=newUnion.id))
        flash('Workplace updated.')
        return redirect('/workplace/all')
    editWorkplace = Workplace.objects.get(id=workplaceid)    
    form.branchname.data = editWorkplace.branchname
    form.company.data = editWorkplace.company
    form.industry.data = editWorkplace.industry
    form.bio.data = editWorkplace.bio
    form.address.data = editWorkplace.address
    form.city.data = editWorkplace.city
    form.state.data = editWorkplace.state
    form.zipcode.data = editWorkplace.zipcode
    form.lat.data = editWorkplace.lat
    form.lon.data = editWorkplace.lon
    form.conemail.data = editWorkplace.conemail
    form.conpnumber.data = editWorkplace.conpnumber

    return render_template('workplaceform.html',form=form, edit=1)

@app.route('/union/delete/pleasenobodyhackthis/<unionid>', methods=['GET', 'POST'])
@login_required
def deleteUnion(unionid):
    unionDelete = Union.objects.get(id=unionid)
    unionDelete.delete()
    flash('Union deleted.')

    return redirect('/union/all')

@app.route('/workplace/delete/pleasenobodyhackthis/<workplaceid>', methods=['GET', 'POST'])
@login_required
def deleteWorkplace(workplaceid):
    workplaceDelete = Workplace.objects.get(id=workplaceid)
    workplaceDelete.delete()
    flash('Workplace deleted.')

    return redirect('/workplace/all')

