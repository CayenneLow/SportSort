#### self-made imports ####
from app import app, db
from models import Users, Events
from forms import LoginForm, RegisterForm, CreateForm
###########################
from flask import Flask, render_template, request, flash, redirect, session
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if user.password == form.password.data:
                session['user'] = str(user.id)
                return 'Login Successful' + ' ' + user.firstname
            else:
                flash('Invalid login credentials')
                redirect('/index')
    return render_template('index.html', title='Index', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Users(
                    firstname = form.firstname.data,
                    lastname = form.lastname.data,
                    email = form.email.data,
                    password = form.password.data
                
                )
        db.session.add(new_user)
        db.session.commit()
        flash('Welcome to SportSort' + ' ' + form.firstname.data)
        return redirect('/index')
    return render_template('register.html', title='Register', form=form)

@app.route('/create', methods=['GET','POST'])
def create():
    form = CreateForm()
    if form.validate_on_submit():
        eventOwner = Users.query.filter_by(id = int(session['user'])).first() 
        new_event = Events(sport = form.sport.data,
                            starttime = form.starttime.data,
                            endtime = form.endtime.data,
                            date = form.date.data,
                            place = form.place.data,
                            n_ppl = form.n_ppl.data,
                            eventOwner = eventOwner)
        db.session.add(new_event)
        db.session.commit()
        flash('Event successfully created by '+ new_event.eventOwner.firstname)
        return redirect('/index')
    return render_template('create.html', title='Create', form=form)

@app.route('/logout')
def logout():
    session.pop(session['user'], None)
    flash('Logged Out')
    print(session['user'] + ' '+ 'logged out')
    return redirect('/index')


