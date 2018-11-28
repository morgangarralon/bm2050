from .model import db

class Account(db.Model):
    __tablename__ = 'Account'
    Id = db.Column(db.Integer, primary_key=True)
    IsAdmin = db.Column(db.Boolean)
    FirstName = db.Column(db.String(255))
    LastName = db.Column(db.String(255))
    EmailAddress = db.Column(db.Integer)
    RoleId = db.Column(db.Integer)
    CreationDate = db.Column(db.DateTime)
    LastLogin = db.Column(db.DateTime)
    Username = db.Column (db.String(255))
    Password = db.Column(db.String(255))

    def __init__(self, EmailAddress):
        self.EmailAddress = EmailAddress

    def __repr__(self):
        return '<User %r>'% self.EmailAddress