from flask import render_template
from app import app

@app.route('/')
@app.route('/baza1')
def baza1():
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    return render_template("baza1.html",
        title = 'Home',
        user = user)
