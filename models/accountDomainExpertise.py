from .model import db

class AccountDomainExpertise(db.Model):
    __tablename__ = 'AccountDomainExpertise'
    AccountId = db.Column(db.Integer, primary_key=True)
    DomainExpertiseId = db.Column(db.Integer, db.ForeignKey('DomainExpertise.Id'))
