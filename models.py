from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(100))
    password = db.Column(db.String(20))
    events = db.relationship("Events", backref="eventOwner")

class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    sport = db.Column(db.String(10))
    starttime = db.Column(db.Time)
    endtime = db.Column(db.Time)
    date = db.Column(db.Date)
    place = db.Column(db.String(30))
    n_ppl = db.Column(db.String(40))
    eventOwner_id = db.Column(db.String(40), db.ForeignKey("users.id"))
