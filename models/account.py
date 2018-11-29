from .model import db
from models.accountDomainExpertise import AccountDomainExpertise

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
    DomainExpertise = []

    def setDomainExpertise(self):
        self.DomainExpertise = AccountDomainExpertise.query.filter_by(AccountId=self.Id).all()
