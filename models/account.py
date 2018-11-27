

from .model import db

class Account(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    IsAdmin = db.Column(db.Boolean)
    FirstName = db.Column(db.Integer)
    LastName = db.Column(db.Integer)
    EmailAddress = db.Column(db.Integer)
    RoleId = db.Column(db.Integer)
    CreationDate = db.Column(db.DateTime)
    LastLogin = db.Column(db.DateTime)
    Username = db.Column (db.String(255))
    Password = db.Column(db.String(255))

    # def __init__(self, isAdmin, firstName, lastName, emailAddress, roleId, CreationDate, lastLoginDate, userName, password):
        # IsAdmin = IsAdmin
        # FirstName = firstName
        # LastName = lastName
        # EmailAddress = emailAddress
        # RoleId = roleId
        # CreationDate = creationDate
        # LastLogin = lastLogin
        # Username = username
        # Password = password

    def __repr__(self):
        return '<User %r>'% self.EmailAddress

