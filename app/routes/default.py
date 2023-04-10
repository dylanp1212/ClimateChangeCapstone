from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/unionizationwhy')
def unionizationwhy():
    return render_template('unionizationwhy.html')

@app.route('/unionizationhow')
def unionizationhow():
    return render_template('unionizationhow.html')