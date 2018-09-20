from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, DateField, IntegerField, SelectField
from wtforms_components import TimeField, DateRange

class RegisterForm(FlaskForm):
    firstname = StringField('First Name', [validators.InputRequired()])
    lastname = StringField('Last Name', [validators.InputRequired()])
    email = StringField('E-mail', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', [validators.InputRequired()])


class LoginForm(FlaskForm):
    email = StringField('E-mail', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])

choices = [('bball','Basketball'), 
           ('fball','Football'),
           ('nball','Netball'),
           ('tball','Tennis')]
class CreateForm(FlaskForm):
    sport = SelectField('Sport', choices=choices)
    starttime = TimeField('Start Time', [validators.InputRequired()]) 
    endtime = TimeField('End Time', [validators.InputRequired()]) 
    #starttime = datetime.strptime(str(starttime), '%H:%M')
    #endtime = datetime.strptime(str(endtime), '%H:%M')
    date = DateField('Date', validators=[DateRange(min=date.today())]) #y-m-d
    place = StringField('Place', [validators.InputRequired()]) 
    n_ppl = IntegerField('# of people needed', [validators.InputRequired()])
